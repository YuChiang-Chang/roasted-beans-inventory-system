<template>
    <div class="admin-user-management">
        <h1>用戶管理</h1>
        <button v-if="hasPermission('add_user')" @click="showCreateForm = !showCreateForm">新增用戶</button>
        <CreateUserForm v-if="showCreateForm" @user-created="refreshUsers"></CreateUserForm>
        <EditUserForm v-if="editingUser" :user="editingUser" @user-updated="refreshUsers"></EditUserForm>
        <UserList @edit-user="handleEditUser"></UserList>
        <!-- <div v-for="user in users" :key="user.id" class="user-item">
            <h3>{{ user.email }}</h3>
            <div class="permissions">
                <div v-for="permission in permissions" :key="permission.id" class="permission-item">
                    <input type="checkbox"
                        :id="`perm-${user.id}-${permission.id}`"
                        :checked="hasPermission(user, permission.id)"
                        @change="togglePermission(user, permission.id)">
                    <label :for="`perm-${user.id}-${permission.id}`">{{ permission.name }}</label>
                </div>
            </div>
        </div> -->
    </div>
</template>

<script>
    import { ref } from 'vue';
    import { useStore } from 'vuex';
    import CreateUserForm from '@/components/CreateUserForm.vue';
    import UserList from '@/components/UserList.vue';
    import EditUserForm from '@/components/EditUserForm.vue';

    export default {
        components:{
            UserList,
            CreateUserForm,
            EditUserForm,
        },
        setup() {
            const store = useStore();
            const showCreateForm = ref(false);
            const editingUser = ref(null);

            const refreshUsers = () => {
                store.dispatch('userManagement/fetchUsers')
            }

            const hasPermission = (permission) => {
                const result = store.getters.hasPermission(permission);
                console.log(`用戶是否擁有 ${permission} 權限: ${result}`);
                return result;
            }

            // onMounted(() => {
            //     store.dispatch('userManagement/fetchUsers');
            //     store.dispatch('userManagement/fetchPermissions');
            // })

            // 從 Vuex store 獲取用戶和權限的狀態
            // const users = computed(() => store.state.userManagement.users);
            // const permissions = computed(() => store.state.userManagement.permissions);

            // 檢查用戶是否有給定的權限
            // const userPermissions = (user) => {
            //     return user.permissions.map(p => p.id);
            // };

            // const hasPermission = (user, permissionId) => {
            //     return userPermissions(user).includes(permissionId);
            // }

            // 切換用戶權限的處理函數
            // const togglePermission = async (user, permissionId) => {
            //     // 檢查用戶是否已擁有該權限
            //     // const hasPermission = user.permissions.some(p => p.id === permission.id);

            //     // 根據是否已擁有該權限來更新 permissions 陣列
            //     const updatedPermissions = hasPermission(user, permissionId)
            //     ? user.permissions.filter(p => p.id !== permissionId)
            //     : [...user.permissions, { id: permissionId }];

            //     // 發送更新請求
            //     await store.dispatch('userManagement/updateUserPermission', { userId: user.id, permissions: updatedPermissions });
            //     // 重新載入用戶列表
            //     await store.dispatch('userManagement/fetchUsers');
            // }

            const handleEditUser = (user) => {
                editingUser.value = user;
            };

            return {
                showCreateForm,
                // users,
                // permissions,
                // hasPermission,
                // userPermissions,
                // togglePermission,
                editingUser,
                handleEditUser,
                refreshUsers,
                hasPermission,
            }
        }
    }
</script>