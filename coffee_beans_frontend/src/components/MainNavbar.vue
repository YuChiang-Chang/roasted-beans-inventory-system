<template>
    <nav v-if="isLoggedIn" class="nav">
        <router-link to="/">首頁</router-link>
        <router-link to="/admin/users">用戶管理</router-link>
        <router-link to="/profile">個人資料</router-link>
        <button @click="logout">登出</button>
    </nav>
</template>

<script>
    import { computed } from 'vue';
    import { useStore } from 'vuex';
    import { useRouter } from 'vue-router';

    export default {
        setup() {
            const store = useStore();
            const router = useRouter();

            const isLoggedIn = computed(() => store.state.isLoggedIn);

            function logout() {
                store.dispatch('logout');
                router.push('/login');
            }

            return {
                isLoggedIn, 
                logout 
            };
        }
    }
</script>

<style lang="scss">
    nav {
        display: flex;
        position: fixed;
        left: 0;
        margin: 1rem;
        top: 0;
        right: 0;
        height: 5rem;
        z-index: 999;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        border:  1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 10px rgba(0, 0, 0, 0.1);
        justify-content: space-evenly;
        align-items: center;

        a, button {
            padding: 1rem;
            margin: 0;
            cursor: pointer;
            background: none;
            backdrop-filter: none;
            font-size: 1rem;
            text-decoration: none;
            text-align: center;
            transition: 0.3s;
            border-radius: 15px;
            font-weight: bolder;

            &:hover {
                background: rgba(255, 255, 255, 0.25);
            }
        }
    }
</style>