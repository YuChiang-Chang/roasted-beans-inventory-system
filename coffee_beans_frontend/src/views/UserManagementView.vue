<template>
    <div class="admin-user-management">
        <h1>用戶管理</h1>
        <button v-if="hasPermission('add_user')" @click="showCreateForm = !showCreateForm">新增用戶</button>
        <CreateUserForm v-if="showCreateForm" @user-created="refreshUsers"></CreateUserForm>
        <EditUserForm v-if="editingUser" :user="editingUser" @user-updated="refreshUsers"></EditUserForm>
        <UserList @edit-user="handleEditUser"></UserList>
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

            const handleEditUser = (user) => {
                editingUser.value = user;
            };

            return {
                showCreateForm,
                editingUser,
                handleEditUser,
                refreshUsers,
                hasPermission,
            }
        }
    }
</script>