import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
import UserManagementView from '../views/UserManagementView.vue';
import UserProfileView from '@/views/UserProfileView.vue';
import store from '../store';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
        meta: { requiresAuth: true },
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/profile',
        name: '/UserProfile',
        component: UserProfileView,
        meta: { requiresAuth: true },
    },
    {
        path: '/admin/users',
        name: 'UserManagement',
        component: UserManagementView,
        meta: { requiresAdmin: true },
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router;

// 假設有一個函數用來檢查用戶是否已經登入
function isLoggedIn() {
    return store.state.isLoggedIn;
}

// function isAdmin() {
//     return store.state.isAdmin;
// }

router.beforeEach((to, from, next) => {

    if (to.name === 'Login' && isLoggedIn()) {
        next({ name: 'Home' });
    } else if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn()) {
        // 如果目標路由需要認證但用戶未登入，重定向到登入頁面
        next({ name: 'Login' });
    // } else if (to.matched.some(record => record.meta.requiresAdmin) && !isAdmin()) {
        // 如果目標路由需要管理員權限但用戶不是管理員，重定向到首頁或其他頁面
        // next({ name: 'Home' });
    } else {
        // 確保一定要調用 next()
        next();
    }
})