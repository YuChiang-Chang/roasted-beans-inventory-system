<template>
    <div class="login-form">
        <h2>登入</h2>
        <form @submit.prevent="login">
            <div class="form-group">
                <label for="email">電子郵件：</label>
                <input id="email" v-model="email" type="email" required>
            </div>
            <div class="form-group">
                <label for="password">密碼：</label>
                <input id="password" v-model="password" type="password" required>
            </div>
            <button type="submit">登入</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
</template>

<script>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router'
    import { useStore } from 'vuex';

    export default {
        setup() {
            const email = ref('');
            const password = ref('');
            const errorMessage = ref('');
            const router = useRouter();
            const store = useStore();
            
            const login = async () => {
                try {
                    await store.dispatch('login', {
                        email: email.value,
                        password: password.value,
                    });
                    router.push({ name: 'Home'});
                } catch (error) {
                    console.error('登入失敗', error.response);
                    errorMessage.value = '登入失敗，請檢查您的電子郵件或密碼。';
                }
            };

            return {
                email,
                password,
                errorMessage,
                login,
            }
        }
    }
</script>

<style>
    .login-form {
        width: 100%;
        padding: 50px;
        margin: 20px;
        border-radius: 15px;
        backdrop-filter: blur(5px);
        background: rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
</style>