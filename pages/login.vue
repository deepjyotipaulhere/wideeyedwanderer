<template>
    <div>
        <div class="login-clean" style="background-color:#1ab4a3;padding:20vh 0">
            <form v-if="$route.query.gen=='s1w'" style="margin-bottom:30px;font-size:smaller;color:rgb(26, 180, 163);padding:20px 40px">
                Account created successfully!
            </form>
            <form method="post">
                <h2 class="sr-only">Login Form</h2>
                <div class="illustration"><i class="icon ion-ios-navigate"></i></div>
                <div class="form-group">
                    <input class="form-control" type="email" name="email" placeholder="Email" v-model="user.username" />
                </div>
                <div class="form-group">
                    <input class="form-control" type="password" name="password" placeholder="Password" v-model="user.password" />
                </div>
                <div class="form-group">
                    <button class="btn btn-primary btn-block" type="submit" @click.prevent="login">Log In</button>
                </div>
                <nuxt-link class="forgot" to="/register">Register for an account</nuxt-link>
                <nuxt-link class="forgot" to="#">Forgot your email or password?</nuxt-link>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    head:{
        link:[
            { rel:'stylesheet', href:'/bootstrap/css/Login-Form-Clean.css' }
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
        login(){
            this.$axios.post("/login",this.user).then(response=>{
                this.$cookies.set('_bid', response.data)
                location.href="/"
            })
        }
    }
}
</script>

<style>

</style>
