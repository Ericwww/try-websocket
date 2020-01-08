<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view />
    <el-input v-model="text"></el-input>
    <el-button type="primary" @click="initWebsocket">Open</el-button>
    <el-button type="primary" @click="sendMessage">Send</el-button>
    <el-button type="primary" @click="closeWebsocket">Close</el-button>
  </div>
</template>

<style lang="less">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;

    a {
      font-weight: bold;
      color: #2c3e50;

      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
</style>

<script>
  export default {
    data() {
      return {
        socket: '',
        text:'',
      }
    },
    methods: {
      initWebsocket() {
        this.socket = new WebSocket("ws://127.0.0.1:5000/echo");
        this.socket.onopen = this.open;
        this.socket.onerror = this.error;
        this.socket.onmessage = this.getMessage;
        this.socket.onclose = this.close;
        
      },
      open: function () {
        console.log("socket连接成功")
      },
      error: function () {
        console.log("连接错误")
      },
      getMessage: function (msg) {
        console.log(msg.data)
      },
      send: function (params) {
        this.socket.send(params)
      },
      close: function () {
        console.log("socket已经关闭")
      },
      sendMessage(){
        let params = this.text;
        this.send(params);
      },
      closeWebsocket(){
        this.socket.close();
      }
    },
    mounted() {
      // this.initWebsocket();
    },
    destroyed() {
      this.socket.onclose=this.close;
    },
  }
</script>