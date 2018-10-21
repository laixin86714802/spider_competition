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

        for (let i in BASE.video_item){
            if (BASE.video_item[i]['uri']){
                $('.sidenav').append(`
                <li id="${BASE.video_item[i]['id']}">
                    <a class="withripple" href="${BASE.video_item[i]['uri']}">
                        <i class="${BASE.video_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                    </a>
                </li>`);
            } else {
                _id = BASE.video_item[i]['id'];
                $('.sidenav').append(`
                <li id="${_id}">
                    <a class="withripple hover" href="#">
                        <i class="${BASE.video_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                        <i class="iright pull-right">&gt;</i>
                    </a>
                    <ul class="sidebar-dropdown"></ul>
                </li>`);

                for (let j in BASE.video_item[i]['children']){
                    $('#' + _id + ' ul').append(`<li><a href="${BASE.video_item[i]['children'][j]}" class="withripple" target="myframe">${j}</a></li>`)
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
        $('ul.nav.navbar-nav li:nth-child(2)').addClass('active');
    },
    init_request: function () {
        $.ajax({
            url: BASE.interface_video_duration,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '视频时长',
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
                            data : result.data.duration,
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
                            name:'视频时长',
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
        });
    },
    active_click: function(){
        $('#duration').click(function (){
            $.ajax({
            url: BASE.interface_video_duration,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '视频时长',
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
                            data : result.data.duration,
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
                            name:'视频时长',
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
                chart.setOption(option, true)
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#videos').click(function (){
            $.ajax({
            url: BASE.interface_video_videos,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '一个地址下视频数量',
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
                            name: '视频数量',
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

        $('#tname').click(function (){
            $.ajax({
            url: BASE.interface_video_tname,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '视频分区',
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
                            name: '分区',
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

        $('#coin').click(function (){
            $.ajax({
            url: BASE.interface_video_coin,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '硬币数量',
                        x:'center'
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
                            data : result.data.coin,
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
                            name:'硬币数量',
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
                chart.setOption(option, true)
            },
            error: function (result) {
                console.log(result)
            }
        })});

        $('#danmaku').click(function (){
            $.ajax({
            url: BASE.interface_video_danmaku,
            type: 'get',
            success: function (result) {
                let option = {
                    title : {
                        text: '弹幕数量',
                        x:'center'
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
                            data : result.data.danmaku,
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
                            name:'弹幕数量',
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
                chart.setOption(option, true)
            },
            error: function (result) {
                console.log(result)
            }
        })});

    }
};

// 启动
new Controller();