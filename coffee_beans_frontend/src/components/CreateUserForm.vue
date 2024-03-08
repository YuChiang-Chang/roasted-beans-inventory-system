<template>
    <div>
        <h2>新增用戶</h2>
        <form @submit.prevent="createUser">
            <div>
                <label for="email">電子郵件</label>
                <input id="email" v-model="newUser.email" type="email" required>
            </div>
            <div>
                <label for="password">密碼</label>
                <input id="password" v-model="newUser.password" type="password" required>
            </div>
            <div>
                <label for="role">角色</label>
                <select name="role" v-model="selectedRoles">
                    <option value="">請選擇角色</option>
                    <option v-for="role in roles" :key="role.id" :value="role.id">{{ role.name }}</option>
                </select>
            </div>
            <div>
                <label>權限</label>
                <div v-for="permission in permissions" :key="permission.id">
                    <input type="checkbox" :value="permission.id" v-model="selectedPermissions">
                    <label>{{ permission.name }}</label>
                </div>
            </div>
            <button type="submit">提交</button>
            <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        </form>
    </div>
</template>

<script>
    import { ref, onMounted } from 'vue';
    import axios from 'axios';
    // import { useStore } from 'vuex';

    export default {
        emits: ['user-created'],
        setup(props, { emit }) {
            const newUser = ref({
                email: '',
                password: '',
            });
            const permissions = ref([]);
            const roles = ref([]);
            const selectedPermissions = ref([]);
            const selectedRoles = ref([]);
            // const store = useStore();
            const errorMessage = ref('');

            const fetchRolesAndPermissions = async () => {
                try {
                    const rolesResponse = await axios.get('/api/user_management/roles/');
                    roles.value = rolesResponse.data;
                    const permissionsResponse = await axios.get('/api/user_management/permissions/');
                    permissions.value = permissionsResponse.data;
                } catch (error) {
                    console.error('獲取角色和權限列表失敗', error);
                }
            };
            onMounted(() => {
                // 獲取權限和角色列表
                fetchRolesAndPermissions(); 
            })

            const createUser = async () => {
                try {
                    await axios.post('/api/user_management/users/', {
                        email: newUser.value.email,
                        password: newUser.value.password,
                        roles: selectedRoles.value ? [selectedRoles.value] : [],
                        permissions: selectedPermissions.value,
                    });
                    emit('user-created');
                    // store.dispatch('userManagement/createUser', newUser.value);
                    // 重置表單
                    newUser.value.email = '';
                    newUser.value.password = '';
                    selectedRoles.value = '';
                    selectedPermissions.value = [];
                    errorMessage.value = '';
                    console.log('創建用戶成功。');
                } catch (error) {
                    console.log('創建用戶失敗。');
                    errorMessage.value = '創建用戶失敗。請檢查輸入。'
                }
            };

            return {
                newUser,
                createUser,
                errorMessage,
                roles,
                permissions,
                selectedRoles,
                selectedPermissions,
            };
        }
    }
</script>