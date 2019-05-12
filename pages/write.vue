<template>
    <div>
        <div style="padding:7em 0 5em 0;background-color:darkcyan">
            <div class="container">
                <h1 class="text-white text-center" v-if="$route.query.id">Edit blog</h1>
                <h1 class="text-white text-center" v-else>Write new blog</h1>
            </div>
        </div>
        <br>
        <div class="container-fluid" style="margin-bottom:2em">
            <div class="row">
                <div class="col-lg-6 col-md-6">
                    <div class="input-group">
                        <input type="text" required v-model="content.title" class="form-control" placeholder="Blog Title" style="padding:1.5em 0.5em;font-size:larger" />
                    </div>
                    <div class="input-group">
                        <input type="text" required v-model="content.place" class="form-control" placeholder="What is the name of the place?" style="padding:0.8em 0.5em;" />
                    </div>
                    <div class="input-group">
                        <input type="text" required v-model="content.address" class="form-control" placeholder="Full address of the place" style="padding:0.8em 0.5em;" />
                    </div>
                    <br>
                    <textarea v-model="content.text" class="form-control" style="width:100%;height:100%"></textarea>                    
                </div>
                <div class="col-lg-6 col-md-6">
                    <h2>{{content.title}}</h2>
                    <div v-html="content.text">
                    </div>
                </div>
            </div>
        </div>
        <center class="clearfix">
            <button class="btn btn-primary" @click.prevent="save" style="clear:both">Save</button>
        </center>



        <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-delay="3000" style="position: absolute; top: 0; right: 0;">
            <div class="toast-header">
                <strong class="mr-auto">Save complete!</strong>
                <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="toast-body text-success">
                <i class="fa fa-check"></i> Your post has been saved successfully!
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            content:{
            }
        }
    },
    created(){
        if(this.$route.query.id)
        {
            this.$axios.get("/getblog/"+this.$route.query.id).then(response=>{
                this.content=response.data
            })
        }
        if(process.browser)
            $('.toast').toast()
    },
    methods:{
        save(){
            this.content.by=this.$cookies.get("_bid")
            if(this.$route.query.id)
            {
                this.$axios.post("/updateblog",this.content).then(response=>{
                    $('.toast').toast('show')
                }).catch(()=>{
                    alert("Error")
                })
            }
            else{
                this.$axios.post("/createblog",this.content).then(response=>{
                    $('.toast').toast('show')
                    this.$router.push("/write?id="+response.data)
                }).catch(()=>{
                    alert("Error")
                })
            }
        }
    }
}
</script>

<style>

</style>
