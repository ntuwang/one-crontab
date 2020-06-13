<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input
        v-model="listQuery.search"
        placeholder="请输入内容"
        clearable
        prefix-icon="el-icon-search"
        style="width: 200px;"
        class="filter-item"
        @keyup.enter.native="handleFilter"
        @clear="handleFilter"
      />
      <el-select class="filter-item" v-model="listQuery.task_name" clearable placeholder="请选择">
        <el-option
          v-for="item in taskscript_list"
          :key="item.id"
          :label="item.name"
          :value="item.code"
        ></el-option>
      </el-select>
      <el-button-group>
        <el-button
          class="filter-item"
          type="primary"
          icon="el-icon-search"
          @click="handleFilter"
        >{{ "搜索" }}</el-button>
      </el-button-group>
    </div>

    <el-table
      :data="list"
      v-loading="listLoading"
      border
      style="width: 100%"
      highlight-current-row
      @sort-change="handleSortChange"
    >
      <el-table-column label="名称" prop="task_name"></el-table-column>
      <el-table-column label="参数" prop="task_args"></el-table-column>
      <el-table-column label="状态" prop="status"></el-table-column>
      <el-table-column label="开始时间" prop="date_created"></el-table-column>
      <el-table-column label="完成时间" prop="date_done"></el-table-column>
      <el-table-column label="操作" align="center" width="100" class-name="small-padding fixed-width">
        <template slot-scope="{ row }">
          <el-button-group>
            <el-button
              v-if="permissionList.update"
              size="small"
              type="success"
              @click="HandleResult(row)"
            >{{ "结果" }}</el-button>
          </el-button-group>
        </template>
      </el-table-column>
    </el-table>
    <div class="table-pagination">
      <pagination
        v-show="total > 0"
        :total="total"
        :page.sync="listQuery.offset"
        :limit.sync="listQuery.limit"
        @pagination="getList"
      />
    </div>
    <el-dialog :visible.sync="dialogFormVisible" :close-on-click-modal="false">
      <div class="runlog">
        <pre>{{result}}</pre>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { taskresult, taskscript, auth } from "@/api/all";
import Pagination from "@/components/Pagination";
import {
  checkAuthAdd,
  checkAuthDel,
  checkAuthView,
  checkAuthUpdate
} from "@/utils/permission";

export default {
  name: "taskresult",

  components: { Pagination },
  data() {
    return {
      operationList: [],
      permissionList: {
        add: false,
        del: false,
        view: false,
        update: false
      },
      list: [],
      total: 0,
      listLoading: true,
      loading: true,
      listQuery: {
        offset: 1,
        limit: 20,
        search: undefined,
        ordering: undefined,
        task_name: ""
      },
      temp: {},
      dialogFormVisible: false,
      rules: {
        name: [{ required: true, message: "请输入名称", trigger: "blur" }]
      },
      taskscript_list: [],
      result: ""
    };
  },
  computed: {},
  created() {
    this.getMenuButton();
    this.getList();
    this.getScript();
  },
  methods: {
    checkPermission() {
      this.permissionList.add = checkAuthAdd(this.operationList);
      this.permissionList.del = checkAuthDel(this.operationList);
      this.permissionList.view = checkAuthView(this.operationList);
      this.permissionList.update = checkAuthUpdate(this.operationList);
    },
    getMenuButton() {
      auth
        .requestMenuButton("taskresult")
        .then(response => {
          this.operationList = response.results;
        })
        .then(() => {
          this.checkPermission();
        });
    },
    getList() {
      this.listLoading = true;
      taskresult.requestGet(this.listQuery).then(response => {
        this.list = response.results;
        this.total = response.count;
        this.listLoading = false;
      });
    },
    getScript() {
      taskscript.requestGet().then(response => {
        this.taskscript_list = response.results;
      });
    },
    handleFilter() {
      this.getList();
    },
    handleSortChange(val) {
      if (val.order === "ascending") {
        this.listQuery.ordering = val.prop;
      } else if (val.order === "descending") {
        this.listQuery.ordering = "-" + val.prop;
      } else {
        this.listQuery.ordering = "";
      }
      this.getList();
    },
    resetTemp() {
      this.temp = {
        task_name: "",
        task_args: "",
        status: "",
        date_created: "",
        date_done: "",
        result: ""
      };
    },
    HandleResult(row) {
      this.dialogFormVisible = true;
      this.result = row.result;
    }
  }
};
</script>
<style scoped>
.runlog {
  padding: 0 20px;
  background-color: #000;
  border: 1px solid rgba(0, 255, 0, 0.41);
  border-radius: 5px;
  color: #00ff00;
}
</style>