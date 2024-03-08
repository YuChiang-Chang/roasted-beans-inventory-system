import axios from "axios";

export const userManagement ={
    namespaced: true,
    state: () => ({
        users: [],
        permissions: [],
        roles: [],
    }),
    mutations: {
        SET_USERS(state, users) {
            state.users = users;
        },
        SET_PERMISSIONS(state, permissions) {
            state.permissions = permissions;
        },
        SET_ROLES(state, roles) {
            state.roles = roles;
        },
    },
    actions: {
        async fetchUsers({ commit }) {
            try {
                const response = await axios.get('/api/user_management/users/');
                commit('SET_USERS', response.data);
            } catch (error) {
                console.error('拉取用戶數據失敗', error);
            }
        },
        async fetchPermissions({ commit }) {
            try {
                const response = await axios.get('/api/user_management/permissions/');
                commit('SET_PERMISSIONS', response.data);
            } catch (error) {
                console.error('拉取權限數據失敗', error);
            }
        },
        async fetchRoles({ commit }) {
            const response = await axios.get('/api/user_management/roles/');
            commit('SET_ROLES', response.data);
        },
        async createUser({ dispatch }, { user }) {
            try {
                await axios.post('/api/user_management/users/', user)
                dispatch('fetchUsers')
            } catch (error) {
                console.error('新增用戶失敗', error);
                let errorMessage = error.response?.data?.detail || error.response?.data?.message || '未知錯誤';
                if (typeof errorMessage === 'object') {
                    errorMessage = Object.entries(errorMessage)
                        .map(([key, value]) => `${key}: ${value}`)
                        .join(', ');
                }
                // if (error.response && error.response.data) {
                //     alert(`新增用戶失敗： ${error.response.data.detail}`);
                // } else {
                    alert('新增用戶失敗，請稍後再試。')
                // }
            }
        },
        async updateUser({ dispatch }, { userId, userData}) {
            try {
                await axios.patch(`/api/user_management/users/${userId}/`, userData);
                dispatch('fetchUsers');
                alert('更新用戶成功');
            } catch (error) {
                console.error('更新用戶失敗', error);
            }
        },
        async updateUserPermissions({ dispatch }, { userId, permissions }) {
            try {
                await axios.put(`/api/user_management/users/${userId}/permissions/`, { permissions });
                dispatch('fetchUsers');
            } catch (error) {
                console.error('更新用戶權限失敗', error);
            }
        },
        async deleteUser({ dispatch }, userId) {
            try {
                await axios.delete(`/api/user_management/users/${userId}/`);
                dispatch('fetchUsers');
                alert('用戶刪除成功');
            } catch (error) {
                console.error('刪除用戶失敗', error);
                alert('刪除用戶失敗，請稍後再試');
            }
        }
    }
}