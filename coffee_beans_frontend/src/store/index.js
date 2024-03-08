import axios from "axios";
import { createStore } from "vuex";
import VuexPersistence from "vuex-persist";
import { userManagement } from "./modules/userManagement";

const vuexLocal = new VuexPersistence({
    storage: window.localStorage
});

const store = createStore({
    modules: {
        userManagement,
    },
    state() {
        return {
            // 這裡放置全局狀態
            email: null,
            isLoggedIn: false,
            userToken: null,
            isAdmin: false,
            userPermissions: [],
        };
    },
    mutations: {
        // 這裡放置改變狀態的方法
        setLoginState(state, { email, isLoggedIn, userToken, isAdmin }) {
            state.email = email;
            state.isLoggedIn = isLoggedIn;
            state.userToken = userToken;
            state.isAdmin = isAdmin;
        },
        setUserPermissions(state, permissions) {
            // console.log("更新權限列表：", permissions);
            state.userPermissions = permissions;
        }
    },
    actions: {
        // 這裡放置執行異步操作的方法
        async login({ commit }, { email, password }) {
            try {
                // 發送登入請求到後端，這裡使用 axios 作為 HTTP 客戶端
                // 後端登入 API 端點
                const response = await axios.post('/api/user_management/login/', { email, password });
                console.log("登入響應：", response.data)

                // 從響應中獲取 token 和用戶資訊（假設後端返回的資料結構中包含這些資訊）
                // const { token, isAdmin, permissions } = response.data;
                // console.log("回傳權限：", permissions)
    
                // 將 token 保存到 localStorage 中，以便之後的請求可以使用
                localStorage.setItem('user-token', response.data.token);
    
                // 調用 mutation 更新 Vuex store 的狀態
                // 傳遞 isLoggedIn 為 true 表示用戶已登入，並傳遞獲得的用戶資訊
                commit('setLoginState', {
                    email: response.data.email,
                    isLoggedIn: true, 
                    userToken: response.data.token, 
                    isAdmin: response.data.isAdmin 
                });
                commit('setUserPermissions', response.data.permissions);
                // console('permissions結果', response.data.permissions)

            } catch (error) {
                console.error('登入失敗', error);
            }

        },
        logout({ commit }) {
            localStorage.removeItem('user-token');
            commit('setLoginState', { isLoggedIn: false, userToken: null, isAdmin: false });
        },
    },
    getters: {
        // currentUser(state) {
        //     return state.user;
        // },
        isUserAdmin(state) {
            return state.isAdmin;
        },
        hasPermission: (state) => (permissionCodename) => {
            console.log('permissionCodename', state)
            return state.userPermissions.includes(permissionCodename);
        }
    },
    plugins: [vuexLocal.plugin]
});

export default store;