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
            <!-- <div v-for="permission in permissions" :key="permission.id">
                <input type="checkbox" :value="permission.id" v-model="selectedPermissions">
                <label>{{ permission.name }}</label>
            </div> -->
            <div>
                <label>選擇角色</label>
                <select v-model="editableUser.selectedRole">
                    <option v-for="role in roles" :key="role.id" :value="role.id">{{ role.name }}</option>
                </select>
            </div>
            <div>
                <label>選擇權限</label>
                <div v-for="permission in permissions" :key="permission.id">
                    <input type="checkbox" 
                        :value="permission.id" 
                        v-model="editableUser.selectedPermissions">
                    {{ permission.name }}
                </div>
            </div>
            <button type="submit">更新用戶</button>
        </form>
    </div>
</template>

<script>
    import { ref, watch, onMounted } from 'vue';
    import { useStore } from 'vuex';
    import axios from 'axios';

    export default {
        props: ['user'],
        setup(props) {
            // const originalUser = reactive({});
            const store = useStore();
            // const permissions = computed(() => store.state.userManagement.permissions);
            const permissions = ref([]);
            const roles = ref([]);
            // const errorMessage = ref('');
            // const selectedPermissions = ref([]);
            const editableUser = ref({
                email: '',
                password: '',
                selectedRole: [],
                selectedPermissions: [],
            });

            const initForm = () => {
                editableUser.value.email = props.user.email || '';
                // editableUser.value.roles = props.user.roles.map(role => role.id) || [];
                editableUser.value.selectedPermissions = props.user.permissions || [];
            }
            
            watch(() => props.user, (newVal) => {
                // editableUser.value.email = newVal.email || '';
                // editableUser.value.password = ''; // 密碼欄位保留空，不預填
                // editableUser.value.selectedRole = newVal.roles?.[0]?.id || '';
                // editableUser.value.selectedPermissions = newVal.permissions?.map(p => p.id) || [];
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
                    // errorMessage.value = '獲取角色和權限列表失敗';
                }
            };

            onMounted(async () => {
                await fetchRolesAndPermissions();
                // initUserForm();
            })

            const submitUpdate = () => {

                const userData = {
                    email: editableUser.value.email,
                    // password: editableUser.value.password,
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
                // console.log('Update user:', props.user.permissions);
                // console.log(permissions);
                // console.log(userData)
                
            }

            return {
                editableUser,
                // selectedPermissions,
                permissions,
                roles,
                submitUpdate,
                // errorMessage,
            }
        }
    }

</script>