<template>
    <TableComponent
        title="User"
        :keys="keys"
        :data="fetchedData"
    ></TableComponent>
</template>

<script>
    import TableComponent from "./TableComponent";
    export default {
        name: "UserList",
        components: {TableComponent},
        data() {
            return {
                keys: ["id", "username", "password", "group"],
                fetchedData: [],
            }
        },
        mounted() {
            this.$http.get('users')
                .then((response) => this.fetchedData = response.data)
                .then((users) => users.forEach((item, index) => {
                    this.$http.get('groups')
                        .then((response) => {
                            let groups = {};
                            response.data.forEach((group) => groups[group.id] = group.name);
                            item.group = groups[item.group_id];
                            console.log(groups);
                            this.$set(this.fetchedData, index, item);
                        })
                }))
                .catch((err) => console.log(err));
        }
    }
</script>

<style scoped>

</style>