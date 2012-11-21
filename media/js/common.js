var isIE=!!window.ActiveXObject;
var isIE6=isIE&&!window.XMLHttpRequest;

function common(){
	searchBox();
	page_init();
	nav_popup();
}

function searchBox(){
	// control searchbox input text
	$("#header .text-input").live('keyup focus',function(){
		if($(this).val()!=='')
			$(this).next().show();
		else
			$(this).next().hide();
	})
	// delete searchbox input text
	$("#header .text-input-clear").click(function(){
		$("#header .text-input").val('').focus();
		$(this).hide();
	})
}

function page_init(){
	var h = $(".article-content").height();
	$("#main-sidebar .sidebar-content").height(h-140);
	$("#main-content").height(h-30);
}

function nav_popup(){
	$("#nav .nav-msg").mouseover(function(){
		$(this).find(".nav-msg-pop").show();
		$(this).addClass("nav-msg-hover");
	})
	$("#nav .nav-msg").mouseout(function(){
		$(this).find(".nav-msg-pop").hide();
		$(this).removeClass("nav-msg-hover");
	})
	$("#nav .nav-admin").mouseover(function(){
		$(this).find(".nav-admin-pop").show();
		$(this).addClass("nav-admin-hover");
	})
	$("#nav .nav-admin").mouseout(function(){
		$(this).find(".nav-admin-pop").hide();
		$(this).removeClass("nav-admin-hover");
	})
	var w = $("#nav .nav-admin").width();
	$("#nav .nav-admin-pop").width(w);
	if(isIE6)
		DD_belatedPNG.fix('.png');
}

function login(){
	//背景图片的自适应
	var height = $(window).height();
	$("#commonBg .wrapper").height(height-80);
	$(window).resize(function(){
		var height = $(window).height();
		$("#commonBg .wrapper").height(height-80);
	})
	//ie6 png透明
	if(isIE6)
		DD_belatedPNG.fix('.png');
}

function email_validate(){
	login();
	window.setInterval("timeCount();", 1000);
	$(".email-bottom a.btn4").click(function(){
		$('.email-validate-number').html(30);
		$(this).parent().hide().prev().show();
	})
}

// 倒计时
function timeCount(selector){
	if($('.email-validate-number').html() == 1){
		$('.email-validate-number').parent().hide().next().show();
		return false;
	}
	$('.email-validate-number').html($('.email-validate-number').html() - 1);
}

function regist(){
	login();
	email_full();
}

function user_info(){
	if(isIE6)
		DD_belatedPNG.fix('.png');
	$("#userInfo .btn-close").click(function(){
		$("#userInfo .tips_tr").fadeOut();
	})
	$(".select-company").toggle(
		function(event){
			$(".select-company-popup").addClass("select-company-open").removeClass("select-company-close");
			$(".select-company-open").fadeIn();
			event.stopPropagation();
		},
		function(event){
			$(".select-company-popup").addClass("select-company-close").removeClass("select-company-open");
			$(".select-company-close").fadeOut();
			event.stopPropagation();
		}
	)
	$(".select-company-popup li").click(function(){
		$(".text-select-company").html($(this).html());
	})
	$("body").click(function(){
		$(".select-company-open").trigger('click');
	})
}

// Email自动补全
function email_full(){	
	var maxcount = 0; // 表示他最大的值
	var thisCount =0; // 初始化他框的位置
	$("body").prepend("<ul id='autoTxt'></ul>");
	$("#sele").live('click keyup',function(even) {
		var v = even.which;
		if (v == 38 || v == 40 || v == 13 ) // 当点击上下键或者确定键时阻止他传送数据
		{
			return;
		}
		var txt = $("#sele").val().split("@")[0]; //这里是取得他的输入框的值
		var email = $("#sele").val().split("@")[1];
		if (txt != "" && email!="" && email!= undefined) {
			//拼装数据
			/*
			$.ajax({
				url : "/email",//从后台取得json数据
				type : "post",
				dataType : "json",
				data : {"emailName" : email},
				success : function(arr_email) {
			*/
			var arr_email = ['sina.com','snda.com','ibm.com','taobao.com','sohu.com','yahoo.com','gmail.com','sina.com.cn'];
			var offset = $("#sele").offset();
			$("#autoTxt").show();
			$("#autoTxt").css("top", (offset.top + 40) + "px");
			$("#autoTxt").css("left", offset.left + "px");
			var Candidate = "";
			maxcount = 0;//再重新得值
			$.each(arr_email, function(k, v) {
				if(v.indexOf(email)>-1)
				{
					Candidate += "<li id='" +maxcount+ "'>" + txt + "@<span class='yellow'>" + v + "</span></li>";
					maxcount++;
				}
			});
			//Candidate += "<li class='more-company'><a href='#'>查看当前开放公司圈></a></li>";
			$("#autoTxt").html(Candidate);
			$("#autoTxt li:eq(0)").css("background", "#fffdf2");
			//高亮对象
			//$('body').highLight();
			//$('body').highLight($("#sele").val());
			//当单击某个li时反映
			$("#autoTxt li").click(function(){
				$("#sele").val($("#autoTxt li:eq("+this.id+")").text());
				$("#autoTxt").html("");
				$("#autoTxt").hide();
			});
			//移动对象
			$("#autoTxt li").hover(
				function(){
					$("#autoTxt li").css("background", "#FFFFFF");
					$("#autoTxt li:eq("+this.id+")").css("background", "#fffdf2");
					thisCount=this.id;
				},
				function(){
					$("#autoTxt li").css("background", "#FFFFFF");
				}
			);
				/*
				},
				error : function() {
					$("#autoTxt").html("");
					$("#autoTxt").hide();
					maxcount = 0;
				}
			});
			*/
		} else {
			$("#autoTxt").hide();
			maxcount = 0;
			$("#sestart").click();
		}
	});
	//当单击body时则隐藏搜索值
	$("body").click(function(){
		$("#autoTxt").html("");
		$("#autoTxt").hide();
		thisCount=0;
	});
	// 写移动事件//上键38 下键40 确定键 13
	$("body").live('keyup click',function(even) {
		var v = even.which;
			if (v == 38)// 按上键时
			{
				if(thisCount!=0){//等于零时则证明不能上了。所以获得焦点
					$("#sele").blur();
					if(thisCount>0)
						--thisCount;
					else
						thisCount=0;
				$("#autoTxt li").css("background", "#FFFFFF");
				$("#autoTxt li:eq("+thisCount+")").css("background", "#fffdf2");
				}else{$("#sele").focus();}
			} else if (v == 40) {// 按下键时
				if(thisCount<maxcount-1)
				{
					$("#sele").blur();
					++thisCount;
					$("#autoTxt li").css("background", "#FFFFFF");
					$("#autoTxt li:eq("+thisCount+")").css("background", "#fffdf2");
				}
			} else if (v == 13) {// 按确认键时
				var tt=$("#"+thisCount).text();
				if(tt!="")
					{
						$("#sele").val(tt);
						$("#autoTxt").html("");
						$("#autoTxt").hide();
					}else
					{
						if($("#sele").val()!="")
						$("#sestart").click();
					}
			} else {
				if($("#autoTxt").html()!="")
					{
						$("#sele").focus();
						thisCount=0;
					}
			}
	});
	$(window).resize(function(){
		$("#autoTxt").hide();
	})
}