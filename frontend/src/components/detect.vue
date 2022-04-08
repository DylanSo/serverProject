<template>
  <div id="baseFramework">
    <UploadDialog
      @handleAdd="handleAdd"
      :visible.sync="visibleOfDialog"
      @handleClose="handleClose"/>
    <!-- 检测功能栏 -->
    <el-row :gutter="0">
      <!-- 左边栏目 -->
      <el-col :span="6">
        <div class="leftNavigator">
          <el-button id="goTotalHistoryButton"
                     icon="el-icon-search"
                     @click="$router.push({path:'./totalHistory'})">
            总检测记录
          </el-button>
          <!-- 最近检测记录栏目 -->
          <div id="latestHistorySummary">最近检测记录</div>
          <!-- 动态更新 -->
          <div id="latestHistoryTogether">

            <!-- 折叠组件 -->
            <el-collapse class="collapse-list" v-model="activeNames">
                  <!--v-model="activeNames"
                      @change="handleChange"-->
                  <el-collapse-item
                    v-for="(item,index) in latestHistory.slice(
                        (pageForm.currentPage-1)*pageForm.pageSize,
                        pageForm.currentPage*pageForm.pageSize
                      )"
                    :key="index"
                    :title="item"
                    :name="index" >
                      <div>{{ item }}</div>
                    <!-- index是当前页条目的index(从0开始)-->
                    <el-table
                      :data="tableData"
                      border
                      style="width: 100%"
                      size="mini"
                      height="100px">
                      <el-table-column
                        fixed
                        prop="date"
                        label="检出日期"
                        width="150">
                      </el-table-column>
                      <el-table-column
                        prop="bNO"
                        label="主板型号"
                        width="100">
                      </el-table-column>
                      <el-table-column
                        prop="defectsTypes"
                        label="缺陷类型"
                        width="200">
                      </el-table-column>
                      <el-table-column
                        prop="defectsNum"
                        label="缺陷个数"
                        width="100">
                      </el-table-column>
                      <el-table-column
                        fixed="right"
                        label="操作"
                        width="50">
                        <template slot-scope="scope">
                          <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
                          <el-button type="text" size="small">编辑</el-button>
                        </template>
                      </el-table-column>
                    </el-table>

                  </el-collapse-item>
                </el-collapse>

            <!-- 分页组件 -->
            <div class="pageTurn">
              <el-pagination
                background
                small
                layout="prev, pager, next"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :pager-count=5
                :total="this.count"
                :current-page="pageForm.currentPage"
                :page-size="pageForm.pageSize"
                :page-sizes=[10,15,20,25,30]
                id="latestHistoryPageTurnTop"
                >
              </el-pagination>

              <el-pagination
                background
                small
                layout="total, sizes, jumper"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :pager-count=5
                :total="this.count"
                :current-page="pageForm.currentPage"
                :page-size="pageForm.pageSize"
                :page-sizes=[10,15,20,25,30]
                id="latestHistoryPageTurnBottom"
              >
              </el-pagination>

            </div>
          </div>
        </div>
      </el-col>

      <!-- 右侧功能栏 -->
      <el-col :span="18">
        <div class="showBoardTogether">

          <el-row :gutter="0">
            <el-col :span="16">
              <div class="grid-content bg-purple">
                <!-- 结果图片 -->
                <el-image
                  style="width: 800px; height: 600px;margin-top: 50px;margin-left: 80px"
                  id="rightResultPhoto"
                  :src="rightResultPhotoUrl"
                  fit="contain">
                </el-image>
              </div>
            </el-col>
            <el-col :span="8">
              <div class="grid-content bg-purple">
                <!-- 数据分析 -->
                <el-image
                  style="width: 400px; height: 300px;margin-top: 80px;margin-left: 40px"
                  id="rightResultDiagram"
                  :src="rightResultDiagrameUrl"
                  fit="contain">
                </el-image>

              </div>
            </el-col>
          </el-row>
          <el-row :gutter="0">
            <el-col :span="6">
              <div class="grid-content bg-purple"
                   style="background: #FFF;
                          width: 1600px;
                          height: 189px;
                          margin-top: 50px">
                <el-button @click="load">增加</el-button>
                <!-- 上传按钮 -->
                <el-dropdown
                  split-button
                  type="primary"
                  @click="handleAdd"
                  @command="handleCommand"
                  placement="top"
                  id="detectUploadBottom"
                >
                  上传
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="uploadFile">上传文件</el-dropdown-item>
                    <el-dropdown-item command="uploadFiles">上传文件夹</el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
              </div>
            </el-col>
          </el-row>

        </div>

      </el-col>
    </el-row>
  </div>
</template>

<script>


export default {
  name: 'detect',
  data () {
    return {
      latestHistory:['1','2','3','4','5','6','7','8','9','10','11','12','13'],  // 最近历史数据
      count: 13,  //最近历史数据总条数
      pageForm: {
        total: this.count, // 总条目数
        pages: this.count/10+1,  // 总页数
        currentPage: 1, // 当前的页码
        pageSize: 10, // 每页显示条目个数
        navigateFirstPage: 1, // 上一页
        navigateLastPage: 2, // 下一页
        lastPage: false, // 是最后一页？
        firstPage: true, // 是第一页？
        hasNextPage: true, // 有下一页？
        hasPreviousPage: false // 有上一页？
      },
      activeNames: [],
      visibleOfDialog: false, // 上传窗口默认不显示
      rightResultPhotoUrl: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      rightResultDiagrameUrl: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
    }
  },
  methods: {
    // 获取最近检测记录
    load () {
      this.count++;
      this.latestHistory.push(this.count.toString());
      this.activeNames.push(this.latestHistory[this.count-1]);
      console.log(this.activeNames)
    },
    /* 分页插件 */
    // currentPage (当前页数)改变时会触发
    handleCurrentChange(newCurrentPage) {
      this.pageForm.currentPage = newCurrentPage;
      this.allShrink();
    },
    // pageSize (每页条数)改变时会触发
    handleSizeChange(newPageSize){
      this.pageForm.pageSize = newPageSize;
      this.allShrink();
    },
    // 上传文件
    handleAdd(){
      this.visibleOfDialog = true;
    },
    handleCommand(command) {
      if (command === "uploadFiles") {
        this.$nextTick(() => {// 上传文件夹
          document.getElementsByClassName(
            "el-upload__input"
          )[0].webkitdirectory = true;
        });
        this.handleAdd();
      } else {
        this.$nextTick(() => {  // 上传文件
          document.getElementsByClassName(
            "el-upload__input"
          )[0].webkitdirectory = false;
        });
        this.handleAdd()
      }
    },
    handleClose() {  // 点击右上角X
      this.visibleOfDialog = false;
    },
    allShrink(){
      this.activeNames = [];
    }
  },
  components: {
    UploadDialog:() => import("./uploadDialog")
  }

}
</script>

<style scoped>
.leftNavigator {
  background-color: rgba(229, 229, 229, 1);
  padding: 0;
}

.showBoardTogether{
  background-color: rgba(229, 229, 229, 1);
  height: 893px;
  padding: 0;
}
#goTotalHistoryButton{
  height: 50px;
  box-sizing: border-box;
  width: 100%;
  border-radius: 0;
  margin-bottom: 1px;
  border: 0;
  font-size: 18px;
  font-weight: lighter;

}
.collapse-list{
  box-sizing: border-box;
  height: 700px;
  background: #FFF;
  overflow-y: scroll;
  overflow-x: hidden;
}

#latestHistorySummary{
  background: #FFF;
  text-align: center;
  height: 42px;
  line-height: 42px;
  font-size: 18px;
  font-weight: lighter;

}
.pageTurn{
  background: #FFF;
  height: 100px;
  text-align: center;
  margin-right: 1px;
  margin-color: rgba(229, 229, 229, 1);
}
#latestHistoryPageTurnTop{
  height: 40px;
  line-height: 40px;
  padding-top: 10px;
}
#latestHistoryPageTurnBottom{
  height: 30px;
  line-height: 40px;
}
#detectUploadBottom{
  left: 752px;
  top: 40px;
  position: relative;
}

</style>
