<template>
    <div>
        <header class="masthead">
            <div class="overlay"></div>
            <div class="container">
                <h5>Write</h5>
            </div>
        </header>
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-6 col-md-6">
                    <textarea v-model="html" style="width:100%;height:100%"></textarea>                    
                </div>
                <div class="col-lg-6 col-md-6">
                    <div v-html="html">

                    </div>
                </div>
            </div>
        </div>
        <br>
        <button class="btn btn-primary" @click.prevent="save">Save</button>
    </div>
</template>

<script>
export default {
    data(){
        return {
            html:''
        }
    },
    created(){
        // this.$axios.get("/chatakpur").then(response=>{
        //     this.html=response.data.text
        // })
    },
    methods:{
        save(){
            // this.$axios.post("/updatechatakpur",{ 'text': this.html }).then(response=>{
            //     alert("Ok")
            // }).catch(()=>{
            //     alert("Error")
            // })
        }
    }
}
</script>

<style>

</style>
