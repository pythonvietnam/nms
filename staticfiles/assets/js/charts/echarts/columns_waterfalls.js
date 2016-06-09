/* ------------------------------------------------------------------------------
 *
 *  # Echarts - columns and waterfalls
 *
 *  Columns and waterfalls chart configurations
 *
 *  Version: 1.0
 *  Latest update: August 1, 2015
 *
 * ---------------------------------------------------------------------------- */

$(function () {

    // Set paths
    // ------------------------------

    require.config({
        paths: {
            echarts: '/static/assets/js/plugins/visualization/echarts'
        }
    });


    // Configuration
    // ------------------------------

    require(
        [
            'echarts',
            'echarts/theme/limitless',
            'echarts/chart/bar',
            'echarts/chart/line'
        ],


        // Charts setup
        function (ec, limitless) {


            // Initialize charts
            // ------------------------------
            var columns_timeline = ec.init(document.getElementById('columns_timeline'), limitless);



            // Charts setup
            // ------------------------------


            //
            // Timeline options
            //

            columns_timeline_options = {

                // Setup timeline
                timeline: {
                    show: false,
                    data: ['2016'],
                    x: 10,
                    x2: 10,
                    label: {
                        formatter: function(s) {
                            return s.slice(0, 4);
                        }
                    },
                    autoPlay: false,
                    playInterval: 3000
                },

                // Main options
                options: [
                    {

                        // Setup grid
                        grid: {
                            x: 55,
                            x2: 110,
                            y: 35,
                            y2: 100
                        },

                        // Add tooltip
                        tooltip: {
                            trigger: 'axis'
                        },

                        // Add legend
                        legend: {
                            show: true,
                            data: ['127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4', '127.0.0.5', '127.0.0.6']
                        },

                        // Add toolbox
                        toolbox: {
                            show: true,
                            orient: 'vertical',
                            x: 'right',
                            y: 70,
                            feature: {
                                mark: {
                                    show: false,
                                    title: {
                                        mark: 'Markline switch',
                                        markUndo: 'Undo markline',
                                        markClear: 'Clear markline'
                                    }
                                },
                                dataView: {
                                    show: false,
                                    readOnly: false,
                                    title: 'View data',
                                    lang: ['View chart data', 'Close', 'Update']
                                },
                                magicType: {
                                    show: true,
                                    title: {
                                        line: 'Switch to line chart',
                                        bar: 'Switch to bar chart',
                                        stack: 'Switch to stack',
                                        tiled: 'Switch to tiled'
                                    },
                                    type: ['line', 'bar'] //, 'stack', 'tiled'
                                },
                                restore: {
                                    show: true,
                                    title: 'Restore'
                                },
                                saveAsImage: {
                                    show: true,
                                    title: 'Same as image',
                                    lang: ['Save']
                                }
                            }
                        },

                        // Enable drag recalculate
                        calculable: true,

                        // Horizontal axis
                        xAxis: [{
                            type: 'category',
                            axisLabel: {
                                interval: 0
                            },
                            data: (function (){
                                var now = new Date();
                                var res = [];
                                var len = 10;
                                while (len--) {
                                    res.unshift(now.toLocaleTimeString().replace(/^\D*/,''));
                                    now = new Date(now - 5000);
                                }
                                return res;
                            })()
                        }],

                        // Vertical axis
                        yAxis: [
                            {
                                type: 'value',
                                name: 'Avenger（time)',
                                max: 100
                            },
                            {
                                show: false,
                                type: 'value',
                                name: 'Other（million)'
                            }
                        ],

                        // Add series
                        series: [
                            {
                                name: '127.0.0.1',
                                type: 'bar',
                                data: (function (){
                                    var res = [];
                                    var len = 10;
                                    while (len--) {
                                        res.push(Math.round(Math.random() * 100));
                                    }
                                    return res;
                                })()
                            },
                            {
                                name: '127.0.0.2',
                                yAxisIndex: 1,
                                type: 'bar',
                                data: (function (){
                                    var res = [];
                                    var len = 10;
                                    while (len--) {
                                        res.push(Math.round(Math.random() * 100));
                                    }
                                    return res;
                                })()
                            },
                            {
                                name: '127.0.0.3',
                                yAxisIndex: 1,
                                type: 'bar',
                                data: (function (){
                                    var res = [];
                                    var len = 10;
                                    while (len--) {
                                        res.push(Math.round(Math.random() * 100));
                                    }
                                    return res;
                                })()
                            },
                            {
                                name: '127.0.0.4',
                                yAxisIndex: 1,
                                type: 'bar',
                                data: (function (){
                                    var res = [];
                                    var len = 10;
                                    while (len--) {
                                        res.push(Math.round(Math.random() * 100));
                                    }
                                    return res;
                                })()
                            },
                            {
                                name: '127.0.0.5',
                                yAxisIndex: 1,
                                type: 'bar',
                                data: (function (){
                                    var res = [];
                                    var len = 10;
                                    while (len--) {
                                        res.push(Math.round(Math.random() * 100));
                                    }
                                    return res;
                                })()
                            },
                            {
                                name: '127.0.0.6',
                                yAxisIndex: 1,
                                type: 'bar',
                                data: (function (){
                                    var res = [];
                                    var len = 10;
                                    while (len--) {
                                        res.push(Math.round(Math.random() * 100));
                                    }
                                    return res;
                                })()
                            }
                        ]
                    }
                ]
            };


            // Apply options
            // ------------------------------

            columns_timeline.setOption(columns_timeline_options);

            // Resize charts
            // ------------------------------

            window.onresize = function () {
                setTimeout(function () {
                    columns_timeline.resize();
                }, 200);
            }

            // Auto
            var timeTicket;
            clearInterval(timeTicket);
            timeTicket = setInterval(function (){
                now = new Date()
                // 动态数据接口 addData
                columns_timeline.addData([
                    [
                        0,        // 系列索引
                        Math.round(Math.random() * 1000), // 新增数据
                        true,     // 新增数据是否从队列头部插入
                        false     // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                    ],
                    [
                        1,        // 系列索引
                        Math.round(Math.random() * 1000), // 新增数据
                        true,    // 新增数据是否从队列头部插入
                        false,    // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                        //false  // 坐标轴标签
                    ],
                    [
                        2,        // 系列索引
                        Math.round(Math.random() * 1000), // 新增数据
                        true,    // 新增数据是否从队列头部插入
                        false,    // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                        //false  // 坐标轴标签
                    ],
                    [
                        3,        // 系列索引
                        Math.round(Math.random() * 1000), // 新增数据
                        true,    // 新增数据是否从队列头部插入
                        false,    // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                        //false  // 坐标轴标签
                    ],
                    [
                        4,        // 系列索引
                        Math.round(Math.random() * 1000), // 新增数据
                        true,    // 新增数据是否从队列头部插入
                        false,    // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                        //false  // 坐标轴标签
                    ],
                    [
                        5,        // 系列索引
                        Math.round(Math.random() * 1000), // 新增数据
                        false,    // 新增数据是否从队列头部插入
                        false,    // 是否增加队列长度，false则自定删除原有数据，队头插入删队尾，队尾插入删队头
                        getTime(now, 5)  // 坐标轴标签
                    ]
                ]);
            }, 5000);

            function getTime(time, add) {
                now = new Date(time + add);
                axisData = now.toLocaleTimeString().replace(/^\D*/,'');
                return axisData;
            }
        }
    );
});
