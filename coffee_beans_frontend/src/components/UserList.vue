<template>
    <div>
        <h2>用戶列表</h2>
        <div v-for="user in users" :key="user.id" class="user-item">
            <p>{{ user.email }}</p>
            <button v-if="hasPermission('edit_user')" @click="$emit('edit-user', user)">編輯</button>
            <button v-if="hasPermission('delete_user')" @click="deleteUser(user.id)">刪除</button>
        </div>
    </div>
</template>

<script>
    import { computed, onMounted } from 'vue';
    import { useStore } from 'vuex';

    export default {
        emits:['edit-user'],
        setup() {
            const store = useStore();
            const users = computed(() => store.state.userManagement.users);

            const hasPermission = computed(() => {
                return (permission) => store.getters.hasPermission(permission);
            })

            const deleteUser = async (userId) => {
                if (confirm('確定要刪除這個用戶嗎?')) {
                    await store.dispatch('userManagement/deleteUser', userId);
                    console.log('Delete user', userId);
                }
            };

            onMounted(() => {
                store.dispatch('userManagement/fetchUsers');
            })

            return {
                users,
                hasPermission,
                deleteUser,
            };
        }
    }
</script>

<style lang="scss">
    .user-item {
        transition: 0.3s;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 10px;
        border-radius: 15px;
        backdrop-filter: blur(5px);
        background: rgba(255, 255, 255, 0.1);
        min-width: 20rem;
    }
</style>