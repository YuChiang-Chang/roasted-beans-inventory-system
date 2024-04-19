<template>
    <div v-if="user">
        <h2>編輯用戶</h2>
        <form @submit.prevent="submitUpdate">
            <div>
                <label for="email">電子郵件</label>
                <input id="email" v-model="editableUser.email" type="email">
            </div>
            <div>
                <label for="password">密碼（留空則不修改）</label>
                <input id="password" v-model="editableUser.password" type="password">
            </div>
            <div>
                <label>選擇角色</label>
                <select v-model="editableUser.selectedRole">
                    <option v-for="role in roles" :key="role.id" :value="role.id" :disabled="isSuperuser">{{ role.name }}</option>
                </select>
            </div>
            <div>
                <label>選擇權限</label>
                <div v-for="permission in permissions" :key="permission.id">
                    <input type="checkbox" 
                        :value="permission.id" 
                        :disabled="isSuperuser"
                        v-model="editableUser.selectedPermissions">
                    {{ permission.name }}
                </div>
            </div>
            <button type="submit">更新用戶</button>
        </form>
    </div>
</template>

<script>
    import { ref, watch, onMounted, computed } from 'vue';
    import { useStore } from 'vuex';
    import axios from 'axios';

    export default {
        props: ['user'],
        setup(props) {
            const store = useStore();
            const permissions = ref([]);
            const roles = ref([]);
            const editableUser = ref({
                email: '',
                password: '',
                selectedRole: [],
                selectedPermissions: [],
            });

            const initForm = () => {
                editableUser.value.email = props.user.email || '';
                editableUser.value.selectedPermissions = props.user.permissions || [];
            }
            
            watch(() => props.user, (newVal) => {
                if (newVal) {
                    initForm();
                }
            }, { deep: true, immediate: true });

            const fetchRolesAndPermissions = async () => {
                try {
                    const [rolesResponse, permissionsResponse] = await Promise.all([
                        axios.get('/api/user_management/roles/'),
                        axios.get('/api/user_management/permissions/')
                    ]);
                    roles.value = rolesResponse.data;
                    permissions.value = permissionsResponse.data;
                } catch (error) {
                    console.error('獲取角色和權限列表失敗', error);
                }
            };

            onMounted(async () => {
                await fetchRolesAndPermissions();
            })

            const submitUpdate = () => {

                const userData = {
                    email: editableUser.value.email,
                }
                
                if (editableUser.value.password) {
                    userData.password = editableUser.value.password;
                }
                
                if (editableUser.value.selectedPermissions) {
                    userData.permissions = editableUser.value.selectedPermissions;
                }
                
                
                store.dispatch('userManagement/updateUser', {
                    userId: props.user.id,
                    userData,
                });
            }

            const isSuperuser = computed(() => {
                return props.user.is_superuser;
            })

            return {
                editableUser,
                permissions,
                roles,
                submitUpdate,
                isSuperuser,
            }
        }
    }

</script>