<template>
    <div id="table">
        <div class="page-header">
            <h2>{{ title }} list</h2>
            <router-link to="add" append>Add {{ title }}</router-link>
        </div>
        <table class="table">
            <thead>
                <tr>
                    <th v-for="key in keys">{{ key }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in data">
                   <td v-for="key in keys">
                       {{ item[key] }}
                   </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: "TableComponent",
        props: {
            title: String,
            keys: Array,
            data: Array,
        }
    }
</script>

<style scoped>

</style>