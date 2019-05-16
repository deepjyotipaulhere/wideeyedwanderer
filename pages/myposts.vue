<template>
    <div>
        <div style="padding:7em 0 5em 0;background-color:orangered">
            <div class="container">
                <h1 class="text-white text-center">My Posts</h1>
            </div>
        </div>
        <div class="container">
            <br>
            <div class="clearfix"><nuxt-link class="btn btn-primary float-right" to="/write">Write New</nuxt-link></div>
            <div class="post-preview" v-for="(x,i) in posts" :key="i">
                <nuxt-link :to="'/write?id='+x._id">
                    <h2 class="post-title">{{x.title}}</h2>
                    <h3 class="post-subtitle">{{x.text}}</h3>
                </nuxt-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            posts:[]
        }
    },

    created(){
        this.$axios.get("/getuserposts/"+this.$cookies.get("bid")).then(response=>{
            this.posts=response.data
        })
    }
}
</script>

<style>

</style>
