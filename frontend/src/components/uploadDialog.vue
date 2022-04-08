<template>
  <div id="uploadDialog">
    <el-dialog title="上传"
               :visible.sync="visibleOfDialog"
               width="720px"
               top="250px"
               style="text-align: center;"
               :before-close="handleClose"
               close-on-press-escape>
      <el-upload
        class="upload"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
        multiple
        >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip" style="margin-bottom: 50px">请上传jpg或png文件</div>
      </el-upload>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "uploadDialog",
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    visibleOfDialog: {
      get: function() {
        return this.visible
      },
      set: function(val) {
        this.$emit('handleAdd', val)
      }
    }
  },
  methods: {
    handleClose(val) {  // 点击右上角X
      this.$emit("handleClose", val)
    }
  }
}
</script>

<style scoped>
.upload{

}
</style>
