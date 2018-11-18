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
                    <th v-if="editable"></th>
                    <th v-if="info"></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in data">
                   <td v-for="key in keys">
                       {{ item[key] }}
                   </td>
                    <td v-if="editable">
                        <router-link :to="{name: editRoute, params: {id: item.id}}" class="btn btn-primary">Edit</router-link>
                    </td>
                    <td v-if="info">
                        <router-link :to="{name: infoRoute, params: {id: item.id}}" class="btn btn-primary">Certify</router-link>
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
            editable: false,
            editRoute: String,
            info: false,
            infoRoute: String,
        }
    }
</script>

<style scoped>

</style>