<template>
    <div class="user-profile">
        <h2>個人資料</h2>
        <div v-if="!isEditing.email">
            <span>Email: {{ user.email }}</span>
            <button @click="toggleEdit('email')">編輯</button>
        </div>
        <div v-else>
            <input v-model="editableFields.email" type="email">
            <button @click="updateField('email')">保存</button>
            <button @click="cancelEdit('email')">取消</button>
        </div>
        <div v-if="!isEditing.password">
            <span>密碼：********</span>
            <button @click="toggleEdit('password')">修改密碼</button>
        </div>
        <div v-else>
            <input v-model="editableFields.password" type="password" placeholder="輸入新密碼">
            <button @click="updateField('password')">保存</button>
            <button @click="cancelEdit('password')">取消</button>
        </div>
    </div>
</template>

<script>
    import { reactive, computed, watch } from 'vue';
    import { useStore } from 'vuex';

    export default {
        setup() {
            const store = useStore();

            // 可編輯字段狀態
            const editableFields = reactive({
                email: '',
                password: '',
            });

            // 是否正在編輯
            const isEditing = reactive({
                email: false,
                password: false,
            }); 

            // 從Vuex獲取當前用戶訊息
            const user = computed(() => store.state.user);

            // 切換可編輯狀態
            const toggleEdit = (field) => {
                isEditing[field] = !isEditing[field];
                // 同時設定當前字段的可編輯值為當前用戶訊息，方便取消時恢復
                // editableFields[field] = user.value[field];
            }

            watch(user, (newValue) => {
                editableFields.email = newValue.email;
            }, { immediate: true });

            // 取消編輯，恢復原狀
            const cancelEdit = (field) => {
                isEditing[field] = false;
                if (field === "email") {
                    editableFields[field] = store.state.user[field];
                } else if (field === "password") {
                    editableFields.password = "";
                }
            }

            const updateField = async (field) => {
                try {
                    await store.dispatch('updateUserInfo', { [field]: editableFields[field] });
                    // 更新成功後切換編輯狀態
                    isEditing[field] = false;
                    if (field === "password") {
                        editableFields.password = "";
                    }
                } catch (error) {
                    console.error('更新失敗', error);
                }
            };
            
            return {
                user,
                isEditing,
                editableFields,
                toggleEdit,
                cancelEdit,
                updateField,
            }
        }
    }
</script>