<template>
  <div id="app">
    <!--    导航栏-->
    <el-row :gutter="0">
      <el-col :span="24">
        <div class="topNavigator" >
          <el-button-group id="topButtonGroup">
            <el-button class="topNavigatorButton" type="primary" @click="$router.push({path:'./'})">检测</el-button>
            <el-button class="topNavigatorButton" type="primary" @click="$router.push({path:'./reports'})">报表</el-button>
            <el-button class="topNavigatorButton" type="primary" @click="$router.push({path:'./help'})">帮助</el-button>
          </el-button-group>
          <p id="topTitle">主板缺陷检测系统</p>
        </div>
      </el-col>
    </el-row>
    <now-time class="times" id="nowTime">{{ time }}</now-time>

    <router-view/>
  </div>
</template>

<script>
import NowTime from "./components/nowTime";
export default {
  name: 'App',
  components: {NowTime},
  data(){
    return{
      time: NowTime.data()
    }
  }
}
</script>

<style>
.topNavigator {
  border-radius: 0;
  min-height: 50px;
  background-color: rgba(0, 153, 204, 1);
}


.topNavigatorButton{
  margin: 0;
  background-color: rgba(72, 170, 212, 1);
  border: 0;
  height: 50px;
  border-radius: 0;
  width: 150px;
  font-size: 20px;
  font-weight: lighter;
}
.topNavigatorButton:hover{
  background-color: rgba(46, 162, 202, 1);
}
#topButtonGroup{
  width: 450px;
}
#topTitle{
  height: 50px;
  font-size: 24px;
  color: aliceblue;
  line-height: 50px;
  float: right;
  padding-right: 100px;
}
#nowTime{
  float: right;
  height: 40px;
  width: 400px;
  right: 0px;
  top: 50px;
  font-size: 20px;
  text-align: center;
  line-height: 40px;
  font-weight: lighter;

  position: fixed;
  z-index: 9999;
}
</style>
