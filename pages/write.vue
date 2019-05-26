<template>
    <div>
        <div style="padding:7em 0 5em 0;background-color:darkcyan">
            <div class="container">
                <h1 class="text-white text-center" v-if="$route.query.id">{{content.title || 'Edit blog'}}</h1>
                <div v-else>
                    <h1 class="text-white text-center">{{content.title || 'Write new blog'}}</h1>
                    <h4 class="text-white text-center">{{content.place || ' '}}</h4>
                    <h6 class="text-white text-center">{{content.address || ' '}}</h6>
                </div>
                <div class="row">
                    <div class="col-lg-9 col-md-9 col-sm-12"></div>
                    <div class="col-lg-3 col-md-3 col-sm-12">
                        <no-ssr>
                            <file-pond
                                name="test"
                                ref="pond"
                                label-idle="Choose cover photo"
                                allow-multiple="false"
                                accepted-file-types="image/jpeg, image/png"
                                :server="baseURL+'/uploadimage'"
                                v-bind:files="myFiles"
                                v-on:init="handleFilePondInit"
                                v-on:processfile="addtopreview1"
                                />
                        </no-ssr>
                    </div>
                </div>
                    
                
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
                    <no-ssr>
                        <file-pond
                            name="test"
                            ref="pond1"
                            label-idle="Drop files here..."
                            allow-multiple="false"
                            accepted-file-types="image/jpeg, image/png"
                            :server="baseURL+'/uploadimage'"
                            v-bind:files="myFiles"
                            v-on:init="handleFilePondInit"
                            v-on:processfile="addtopreview"
                            />
                    </no-ssr>
                </div>
                <div class="col-lg-6 col-md-6">
                    <div v-html="content.text">
                    </div>
                </div>
            </div>
        </div>
        <center class="clearfix" style="margin-top:15em">
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
import vueFilePond from 'vue-filepond';
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css';
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';

const FilePond = vueFilePond(FilePondPluginFileValidateType, FilePondPluginImagePreview);
export default {
    data(){
        return {
            // baseURL:"http://localhost:5000",
            baseURL:"http://www.wideeyedwanderer.in/api",
            content:{
            },
            myFiles: []
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
    components: {
        FilePond
    },
    methods:{
        save(){
            this.content.by=this.$cookies.get("bid")
            if(this.$route.query.id)
            {
                this.$axios.post("/updateblog",this.content).then(response=>{
                    $('.toast').toast('show')
                }).catch(()=>{
                    alert("Error")
                })
            }
            else{
                this.content.view=0
                this.$axios.post("/createblog",this.content).then(response=>{
                    $('.toast').toast('show')
                    this.$router.push("/write?id="+response.data)
                }).catch(()=>{
                    alert("Error")
                })
            }
        },

        handleFilePondInit: function() {
            console.log('FilePond has initialized');

            // FilePond instance methods are available on `this.$refs.pond`
        },
        addtopreview: function(error, file){
            var p='<br><img style="max-width:100%;height:auto" src="'+this.baseURL+'/getimage/'+file.serverId+'" /><br>'
            this.content.text+= p
            this.myFiles=[]
        },
         addtopreview1: function(error, file){
            this.content.coverphoto= file.serverId
        },
        getimage(id){
            this.$axios.get("/getimage/"+id).then(response=>{
                return response.data
            })
        }
    },

    computed:{
        
    }
}
</script>

<style>

</style>
