import { reactive, toRefs } from "vue";

const messageState = reactive({
    message: '',
    showMessage: false,
});

function setMessage(newMessage) {
    messageState.message = newMessage;
    messageState.showMessage = true;

    setTimeout(() => {
        messageState.showMessage = false;
    }, 3000);
}

export function useMessageState() {
    return { messageState: toRefs(messageState), setMessage };
}