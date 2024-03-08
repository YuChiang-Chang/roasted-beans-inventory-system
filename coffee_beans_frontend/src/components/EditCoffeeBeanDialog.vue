<template>
    <Teleport to="body">
        <div class="dialog-backdrop" v-if="isVisible">
            <div class="dialog">
                <h2>編輯咖啡豆</h2>
                <form @submit.prevent="save">
                    <div class="form-group">
                        <label for="name">{{ formLabels.name }}</label>
                        <input id="name" v-model="editableBean.name" type="text">
                    </div>
                    <div class="form-group">
                        <label for="roast_date">{{ formLabels.roastDate }}</label>
                        <input id="roast_date" v-model="editableBean.roast_date" type="date">
                    </div>
                    <div class="form-group">
                        <label for="roast_level">{{ formLabels.roastLevel }}</label>
                        <select id="roast_level" v-model="editableBean.roast_level">
                            <option value="淺烘焙">淺烘焙</option>
                            <option value="中烘焙">中烘焙</option>
                            <option value="深烘焙">深烘焙</option>
                        </select>
                    </div>
                    <div>
                        <label for="weight">{{ formLabels.weight }}</label>
                        <input id="weight" v-model="editableBean.weight" type="number" required>
                    </div>
                    <div class="form-group">
                        <label for="origin">{{ formLabels.origin }}</label>
                        <input id="origin" v-model="editableBean.origin" type="text">
                    </div>
                    <div>
                        <label for="notes">{{ formLabels.notes }}</label>
                        <textarea id="notes" v-model="editableBean.notes"></textarea>
                    </div>
                    <button type="submit">{{ formLabels.submitButton }}</button>
                    <button type="button" @click="close">{{ formLabels.cancelButton }}</button>
                </form>
            </div>
        </div>
    </Teleport>
</template>

<script>
    import { ref, watch } from 'vue';
    import zh from '@/i18n/locales/zh';

    export default {
        props: {
            coffeeBean: Object,
            isVisible: Boolean,
        },

        emits: ['update:isVisible', 'save'],
        setup(props, { emit }) {
            const editableBean = ref({ ...props.coffeeBean });
            const formLabels = zh.formLabels

            watch(
                // 第一個參數是我們想要監視的對象
                () => props.coffeeBean,
                // 第二個參數是當監視的對象發生變化時，我們想要執行的函數
                (newVal) => {
                    // 把新的值賦值給 editableBean
                    editableBean.value = { ...newVal };
            });

            const save = () => {
                emit('save', editableBean.value);
                // emit('update:isVisible', false);
            };

            const close = () => {
                emit('update:isVisible', false);
            };

            return { 
                editableBean, 
                save, 
                close,
                formLabels,
            };
        }
    }
</script>

<style>
.dialog-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog {
  background: white;
  padding: 20px;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 10px;
}

.form-group label {
  display: block;
}
</style>