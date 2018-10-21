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
    },
    menu_load: function (){
        $('.sidenav').append(`
        <span class="navbar-side">
            <a class="withripple" href="#">
                <i class="glyphicon glyphicon-list"></i><span id="nav-control">收起</span>
            </a>
        </span>`);

        for (let i in BASE.graph_item){
            if (BASE.graph_item[i]['uri']){
                $('.sidenav').append(`
                <li id="${BASE.graph_item[i]['id']}">
                    <a class="withripple" href="${BASE.graph_item[i]['uri']}">
                        <i class="${BASE.graph_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                    </a>
                </li>`);
            } else {
                _id = BASE.graph_item[i]['id'];
                $('.sidenav').append(`
                <li id="${_id}">
                    <a class="withripple" href="#">
                        <i class="${BASE.graph_item[i]['icon']}"></i>
                        <span class="sidespan">${i}</span>
                        <i class="iright pull-right">&gt;</i>
                    </a>
                    <ul class="sidebar-dropdown"></ul>
                </li>`);

                for (let j in BASE.graph_item[i]['children']){
                    $('#' + _id + ' ul').append(`<li><a href="${BASE.graph_item[i]['children'][j]}" class="withripple">${j}</a></li>`)
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
        $('ul.nav.navbar-nav li:nth-child(4)').addClass('active');
    }
};

// 启动
new Controller();