$(document).ready(function(){
	$.ajax({
        url:'/get_sp_date',
        type : 'get',
        data : {
        },
        async: true,//设置为同步
        dataType : 'json',
        success:function(data){
            setCharts(data);
        },
        error : function(){
            alert('error');
        }
    });
	
});

function setCharts(data){
	option = {
	    title : {
	        text: '温度变化',
	        subtext: '罗列所有温度相关内容'
	    },
	    tooltip : {
	        trigger: 'axis'
	    },
	    legend: {
	        data:['室内温度','CPU温度','GPU温度']
	    },
	    toolbox: {
	        show : true,
	        feature : {
	            dataZoom: {},
	            dataView: {readOnly: false},
	            magicType: {type: ['line', 'bar']},
	            restore: {},
	            saveAsImage: {}
	        }
	    },
	    xAxis : [
	        {
	            type : 'category',
	            boundaryGap : false,
	            data : data.time
	        }
	    ],
	    yAxis : [
	        {
	            type : 'value',
	            axisLabel : {
	                formatter: '{value} °C'
	            }
	        }
	    ],
	    series : [
	        {
	            name:'室内温度',
	            type:'line',
	            data:data.house
	        },
	        {
	            name:'CPU温度',
	            type:'line',
	            data:data.cpu
	        },
	        {
	            name:'GPU温度',
	            type:'line',
	            data:data.gpu
	        }
	    ]
	};
	temp_chart = echarts.init($('#temp_div')[0]);
	temp_chart.setOption(option);
	
	hum_option = {
	    title : {
	        text: '湿度变化',
	        subtext: '室内湿度相关内容'
	    },
	    tooltip : {
	        trigger: 'axis'
	    },
	    legend: {
	        data:['湿度']
	    },
	    toolbox: {
	        show : true,
	        feature : {
	            dataZoom: {},
	            dataView: {readOnly: false},
	            magicType: {type: ['line', 'bar']},
	            restore: {},
	            saveAsImage: {}
	        }
	    },
	    xAxis : [
	        {
	            type : 'category',
	            boundaryGap : false,
	            data : data.time
	        }
	    ],
	    yAxis : [
	        {
	            type : 'value',
	            axisLabel : {
	                formatter: '{value} %'
	            }
	        }
	    ],
	    series : [
	        {
	            name:'室内湿度',
	            type:'line',
	            data:data.humidity
	        }
	    ]
	};
	hum_chart = echarts.init($('#humidity_div')[0]);
	hum_chart.setOption(hum_option);
}