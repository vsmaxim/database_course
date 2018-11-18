export default {
    mounted() {
        if (!this.$store.state.role) {
            this.$router.push({name: 'login'});
        }
    }
}