/**
 * Created by xx on 2018/10/09.
 */


let Controller = function () {
    this.init();
};

Controller.prototype = {
    // 初始化
    init: function () {
        // 菜单加载
        this.menu_load();
        // 加载样式
        this.style_loading();
        // 激活样式
        this.active_loading();
        // 接口状态请求
        this.interface_status_request(this.echarts_handler, this.error_handler);
        // 表单验证
        this.form_verify();
        // 表单提交
        this.form_submit(this.list_data_handler);
        // 列表渲染
        this.list_data_handler({});
    },
    menu_load: function (){
        $('.sidenav').append(`
        <span class="navbar-side">
            <a class="withripple" href="#">
                <i class="glyphicon glyphicon-list"></i><span id="nav-control">收起</span>
            </a>
        </span>`);

        for (let i in BASE.status_item){
            if (BASE.status_item[i]['uri']){
                $('.sidenav').append(`
                <li id="${BASE.status_item[i]['id']}">
                    <a class="withripple" href="${BASE.status_item[i]['uri']}">
                        <i class="${BASE.status_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                    </a>
                </li>`);
            } else {
                _id = BASE.status_item[i]['id'];
                $('.sidenav').append(`
                <li id="${_id}">
                    <a class="withripple" href="#">
                        <i class="${BASE.status_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                        <i class="iright pull-right">&gt;</i>
                    </a>
                    <ul class="sidebar-dropdown"></ul>
                </li>`);

                for (let j in BASE.status_item[i]['children']){
                    $('#' + _id + ' ul').append(`<li><a href="${BASE.status_item[i]['children'][j]}" class="withripple">${j}</a></li>`)
                }
            }
        }
    },
    style_loading: function () {
        /* 侧边栏切换形态 */
        $('.navbar-side').click(function () {
            $('body').toggleClass('sidebar-collapse');
            $('#nav-control').toggleClass('hide');
            $('table thead>tr').css('width', '100%');
            return false;
        });
        // 二级菜单
        $(".sidenav>li>a").click(function(){
            $(this).parent().siblings().children("a").removeClass("hover").next().slideUp();
            $(this).addClass("hover");
            $(this).next().slideToggle();
        });
    },
    active_loading: function () {
        $('ul.nav.navbar-nav li').removeClass('active');
        $('ul.sidenav li a').removeClass('hover');
        $('ul.nav.navbar-nav li:nth-child(1)').addClass('active');
        $('ul.sidenav li:nth-child(2) a').addClass('hover');
    },
    interface_status_request: function (success_callback, error_callback) {
        $.ajax({
            url: BASE.interface_view,
            type: 'get',
            success: function (result) {
                success_callback(result.data)
            },
            error: function (result) {
                error_callback(result)
            }
        });
    },
    // 饼图渲染
    echarts_handler: function (data) {
        // 饼图参数
        let option = {
            title: {
                text: "",
                //subtext: undefined,
                x: "center",
                y: "center",
                itemGap: 20,
                textStyle: {color: "skyblue", fontFamily: "微软雅黑", fontSize: 18, fontWeight: "bolder"}
            },
            tooltip: {
                trigger: "item",
                show: true,
                formatter: "{a} <br/>{b} : {c} ({d}%)",
                extraCssText: "width:auto;height:60px;background:rgba(0,0,0,.4);"
            },
            legend: {
                orient: "vertical",
                x: "left",
                y: "top",
                data: ["启用", "停用", "暂停"]
            },
            toolbox: {
                show: true,
                feature: {mark: {show: true}}
            },
            color: ["#7dd4f8", "#60b2d3", "#2973a7"],
            series: [{
                name: "接口状态",
                type: "pie",
                clockWise: false,
                radius: [70, 105],
                itemStyle: {normal: {label: {show: false}, labelLine: {show: false}}},
                data: null
            }]
        };
        // 秒级饼图
        let interface_s = document.getElementById('interface-s');
        let s_chart = echarts.init(interface_s);
        option.title.text = "秒";
        option.series[0].data = data['s'];
        $('#interface-s-desc').html(`
            <span class="tip-show-set">启用接口: ${data['s'][0]['value']}</span>
            <span class="tip-show-set">停用接口: ${data['s'][1]['value']}</span>
            <span class="tip-show-set">暂停接口: ${data['s'][2]['value']}</span>
        `);
        s_chart.clear();
        s_chart.setOption(option, true);
        // 天级饼图
        let interface_d = document.getElementById('interface-d');
        let d_chart = echarts.init(interface_d);
        option.title.text = "天";
        option.series[0].data = data['d'];
        $('#interface-d-desc').html(`
            <span class="tip-show-set">启用接口: ${data['d'][0]['value']}</span>
            <span class="tip-show-set">停用接口: ${data['d'][1]['value']}</span>
            <span class="tip-show-set">暂停接口: ${data['d'][2]['value']}</span>
        `);
        d_chart.clear();
        d_chart.setOption(option, true);
        // 月级饼图
        let interface_m = document.getElementById('interface-m');
        let m_chart = echarts.init(interface_m);
        option.title.text = "月";
        option.series[0].data = data['m'];
        $('#interface-m-desc').html(`
            <span class="tip-show-set">启用接口: ${data['m'][0]['value']}</span>
            <span class="tip-show-set">停用接口: ${data['m'][1]['value']}</span>
            <span class="tip-show-set">暂停接口: ${data['m'][2]['value']}</span>
        `);
        m_chart.clear();
        m_chart.setOption(option, true);
    },
    // 失败请求
    error_handler: function (data) {
        console.log(data)
    },

    form_verify: function () {
        $('form').bootstrapValidator({
            message: '输入错误',
            fields: {
                'interface-id': {
                    validators: {
                        numeric: {
                            message: '接口id只能填写数字'
                        }
                    }
                },
                'run-times': {
                    validators: {
                        numeric: {
                            message: '运行次数只能填写数字'
                        }
                    }
                },
                'total-times': {
                    validators: {
                        numeric: {
                            message: '运行总次数只能填写数字'
                        }
                    }
                }
            }
        })
    },
    form_submit: function (handler) {
        // 开启表单验证
        $('form').data('bootstrapValidator').validate();
        // 绑定提交按钮
        $('#form-submit').on({
            click: function () {
                if ($('form').data('bootstrapValidator').isValid()) {
                    let data = {};
                    if ($('input[name=interface-id]').val() !== '') {
                        data.interface_id = $('input[name=interface-id]').val();
                    }
                    if ($('input[name=interface-name]').val() !== '') {
                        data.interface_type = $('input[name=interface-name]').val();
                    }
                    if ($('input[name=run-times]').val() !== '') {
                        data.run_times = $('input[name=run-times]').val();
                    }
                    if ($('input[name=total-times]').val() !== '') {
                        data.total_times = $('input[name=total-times]').val();
                    }
                    if ($("#run_type option:selected").val() !== '') {
                        data.run_type = $("#run_type option:selected").val();
                    }
                    if ($("#status option:selected").val() !== '') {
                        data.status = $("#status option:selected").val();
                    }
                    handler(data)
                } else {
                    return false;
                }
            }
        })
    },
    list_data_handler: function (data) {
        $('#interface-list').bootstrapTable('destroy');
        $('#interface-list').bootstrapTable({
            url: BASE.interface_list,           // 请求后台的URL(*)
            method: 'get',                      // 请求方式(*)
            // toolbar: null,                   // 工具按钮用哪个容器
            striped: true,                      // 是否显示行间隔色
            cache: false,                       // 是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性(*)
            pagination: true,                   // 是否显示分页(*)
            sortable: false,                    // 是否启用排序
            sortOrder: "asc",                   // 排序方式
            queryParams: function (params) {    // 传递参数(*)
                data.limit = params.limit;
                data.offset = params.offset;
                return data;
            },
            sidePagination: "server",           // 分页方式：client客户端分页，server服务端分页(*)
            pageNumber: 1,                      // 初始化加载第一页，默认第一页
            pageSize: 10,                       // 每页的记录行数(*)
            pageList: [10, 25, 50, 100],        // 可供选择的每页的行数(*)
            search: true,                       // 是否显示表格搜索，此搜索是客户端搜索
            strictSearch: true,
            showColumns: true,                  // 是否显示所有的列
            showRefresh: true,                  // 是否显示刷新按钮
            minimumCountColumns: 2,             // 最少允许的列数
            clickToSelect: true,                // 是否启用点击选中行
            height: 500,                        // 行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId: "ID",                     // 每一行的唯一标识，一般为主键列
            showToggle: true,                    // 是否显示详细视图和列表视图的切换按钮
            cardView: false,                    // 是否显示详细视图
            detailView: false,                  // 是否显示父子表
            columns: [{
                field: 'InterfaceID',
                title: '接口ID'
            }, {
                field: 'Comment',
                title: '接口描述'
            }, {
                field: 'InterfaceType',
                title: '接口名称'
            }, {
                field: 'InterfaceType',
                title: '接口名称'
            }, {
                field: 'RunType',
                title: '账期类型'
            }, {
                field: 'Status',
                title: '接口状态'
            }, {
                field: 'Runperiod',
                title: '本次账期'
            }, {
                field: 'LastRunperiod',
                title: '上次账期'
            }, {
                field: 'RunTimes',
                title: '运行次数'
            }, {
                field: 'TotalTimes',
                title: '总次数'
            }, {
                field: 'MaxRetryTimes',
                title: '重试次数'
            }, {
                field: 'MinStart',
                title: '最小开始时间'
            }]
        });
        // 去掉工具栏
        $('.fixed-table-toolbar').remove();
    }
};

// 启动
new Controller();