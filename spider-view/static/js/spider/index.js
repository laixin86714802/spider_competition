/**
 * Created by xx on 2018/10/21.
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
        // 初始化请求
        this.init_request();
        // 绑定点击
        this.active_click();
    },
    menu_load: function (){
        $('.sidenav').append(`
        <span class="navbar-side">
            <a class="withripple" href="#">
                <i class="glyphicon glyphicon-list"></i><span id="nav-control">收起</span>
            </a>
        </span>`);

        for (let i in BASE.user_item){
            if (BASE.user_item[i]['uri']){
                $('.sidenav').append(`
                <li id="${BASE.user_item[i]['id']}">
                    <a class="withripple" href="${BASE.user_item[i]['uri']}">
                        <i class="${BASE.user_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                    </a>
                </li>`);
            } else {
                _id = BASE.user_item[i]['id'];
                $('.sidenav').append(`
                <li id="${_id}">
                    <a class="withripple hover" href="#">
                        <i class="${BASE.user_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                        <i class="iright pull-right">&gt;</i>
                    </a>
                    <ul class="sidebar-dropdown"></ul>
                </li>`);

                for (let j in BASE.user_item[i]['children']){
                    $('#' + _id + ' ul').append(`<li><a href="${BASE.user_item[i]['children'][j]}" class="withripple" target="myframe">${j}</a></li>`)
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
    },
    init_request: function () {
        $.ajax({
            url: BASE.interface_user_sex,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户性别比例',
                        x:'center'
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{b} : {c} ({d}%)"
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        data: ['空','保密','男','女']
                    },
                    color: ["#7dd4f8", "#60b2d3", "#2973a7", "#18b8dc"],
                    series : [
                        {
                            name: '性别比例',
                            type: 'pie',
                            radius : '55%',
                            center: ['50%', '60%'],
                            data: result.data,
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                };
                // 饼图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        });
    },
    active_click: function(){
        $('#sex').click(function (){
            $.ajax({
            url: BASE.interface_user_sex,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户性别比例',
                        x:'center'
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{b} : {c} ({d}%)"
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        data: ['空','保密','男','女']
                    },
                    color: ["#7dd4f8", "#60b2d3", "#2973a7", "#18b8dc"],
                    series : [
                        {
                            name: '性别比例',
                            type: 'pie',
                            radius : '55%',
                            center: ['50%', '60%'],
                            data: result.data,
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            },
                            label: {
                                show: false
                            }
                        }
                    ]
                };
                // 饼图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#regtime').click(function (){
            $.ajax({
            url: BASE.interface_user_regtime,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户注册时间',
                        x:'center'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    color: ['#3398DB'],
                    tooltip : {
                        trigger: 'axis',
                        axisPointer : {
                            type : 'shadow'
                        }
                    },
                    xAxis : [
                        {
                            type : 'category',
                            data : result.data.date,
                            axisTick: {
                                alignWithLabel: true
                            }
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : [
                        {
                            name:'注册人数',
                            type:'bar',
                            barWidth: '60%',
                            data:result.data.value
                        }
                    ]
                };
                // 直方图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#birthday').click(function (){
            $.ajax({
            url: BASE.interface_user_birthday,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户生日',
                        x:'center'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{b} : {c} ({d}%)"
                    },
                    legend: {
                        type: 'scroll',
                        bottom: 10,
                        orient: 'vertical',
                        left: 'left',
                        data: result.data.legend
                    },
                    color: ["#7dd4f8", "#60b2d3", "#2973a7", "#18b8dc"],
                    series : [
                        {
                            name: '性别比例',
                            type: 'pie',
                            radius : '55%',
                            center: ['50%', '60%'],
                            data: result.data.data,
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            },
                            label: {
                                show: false
                            }
                        }
                    ]
                };
                // 饼图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#sign').click(function (){
            $.ajax({
            url: BASE.interface_user_sign,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户签名长度',
                        x:'center'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    color: ['#3398DB'],
                    tooltip : {
                        trigger: 'axis',
                        axisPointer : {
                            type : 'shadow'
                        }
                    },
                    xAxis : [
                        {
                            type : 'category',
                            data : result.data.sign,
                            axisTick: {
                                alignWithLabel: true
                            }
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : [
                        {
                            name:'签名长度',
                            type:'bar',
                            barWidth: '60%',
                            data:result.data.value
                        }
                    ]
                };
                // 饼图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#level').click(function (){
            $.ajax({
            url: BASE.interface_user_level,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户等级比例',
                        x:'center'
                    },
                    tooltip : {
                        trigger: 'item',
                        formatter: "{b} : {c} ({d}%)"
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        data: ['0','1','2','3','4','5','6']
                    },
                    color: ["#7dd4f8", "#60b2d3", "#2973a7", "#18b8dc"],
                    series : [
                        {
                            name: '等级比例',
                            type: 'pie',
                            radius : '55%',
                            center: ['50%', '60%'],
                            data: result.data,
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            },
                            label: {
                                show: false
                            }
                        }
                    ]
                };
                // 饼图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#article').click(function (){
            $.ajax({
            url: BASE.interface_user_article,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户文章观看次数',
                        x:'center'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    color: ['#3398DB'],
                    tooltip : {
                        trigger: 'axis',
                        axisPointer : {
                            type : 'shadow'
                        }
                    },
                    xAxis : [
                        {
                            type : 'category',
                            data : result.data.label,
                            axisTick: {
                                alignWithLabel: true
                            }
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : [
                        {
                            name:'文章观看次数',
                            type:'bar',
                            barWidth: '60%',
                            data:result.data.value
                        }
                    ]
                };
                // 直方图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#fans').click(function (){
            $.ajax({
            url: BASE.interface_user_fans,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户粉丝数',
                        x:'center'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    color: ['#3398DB'],
                    tooltip : {
                        trigger: 'axis',
                        axisPointer : {
                            type : 'shadow'
                        }
                    },
                    xAxis : [
                        {
                            type : 'category',
                            data : result.data.label,
                            axisTick: {
                                alignWithLabel: true
                            }
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : [
                        {
                            name:'粉丝数',
                            type:'bar',
                            barWidth: '60%',
                            data:result.data.value
                        }
                    ]
                };
                // 直方图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#following').click(function (){
            $.ajax({
            url: BASE.interface_user_following,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '用户关注数',
                        x:'center'
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    color: ['#3398DB'],
                    tooltip : {
                        trigger: 'axis',
                        axisPointer : {
                            type : 'shadow'
                        }
                    },
                    xAxis : [
                        {
                            type : 'category',
                            data : result.data.label,
                            axisTick: {
                                alignWithLabel: true
                            }
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value'
                        }
                    ],
                    series : [
                        {
                            name:'关注数',
                            type:'bar',
                            barWidth: '60%',
                            data:result.data.value
                        }
                    ]
                };
                // 直方图
                let space = document.getElementById('space');
                let chart = echarts.init(space);
                chart.clear();
                chart.setOption(option, true);
            },
            error: function (result) {
                console.log(result)
            }
        })});

    }
};

// 启动
new Controller();