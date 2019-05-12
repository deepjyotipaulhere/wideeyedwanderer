<template>
    <div>
        <div class="register-photo" style="background-color:deepskyblue;padding:20vh 0">
            <div class="form-container">
                <div class="image-holder"></div>
                <form method="post">
                    <h2 class="text-center"><strong>Create</strong> an account.</h2>
                    <div class="form-group">
                        <input class="form-control" type="email" name="email" placeholder="Email" v-model="user.username" />
                    </div>
                    <div class="form-group">
                        <input class="form-control" type="password" name="password" placeholder="Password" v-model="user.password" />
                    </div>
                    <div class="form-group">
                        <input class="form-control" type="password" name="password-repeat" placeholder="Password (repeat)" />
                    </div>
                    <div class="form-group">
                        <div class="form-check"><label class="form-check-label">
                            <input class="form-check-input" type="checkbox" />I agree to the license terms.</label>
                        </div>
                    </div>
                    <div class="form-group">
                        <button class="btn btn-primary btn-block" type="submit" @click.prevent="register">Sign Up</button>
                    </div>
                    <nuxt-link class="already" to="/login">You already have an account? Login here.</nuxt-link>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    head:{
        link:[
            { rel:'stylesheet', href:'/bootstrap/css/Registration-Form-with-Photo.css' }
        ]
    },

    data(){
        return {
            user:{
                username:'',
                password:''
            }
        }
    },

    methods:{
        register(){
            this.$axios.post("/register",this.user).then(response=>{
                this.$router.push("/login?gen=s1w")
            })
        }
    }
}
</script>

<style>

</style>
