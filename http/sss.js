var page = require('webpage').create();
var server = require('webserver').create();
var sys = require('system');

if(sys.args.length !== 2){
    console.log('args is error,demo: phantomjs server.js 80');
    phantom.exit(1);
}else{
    console.log("welcome! system is start on port:"+sys.args[1]+"\ntest url is: http://localhost/http://www.baidu.com");
}
 
var port = sys.args[1];
 
//输出到网页预览图片,地址:http://localhost/http://www.baidu.com

service = server.listen(port,function(req, res){
    var url=decodeURIComponent(req.url).substr(1);
    res.statusCode = 200;
    res.headers = {
        'Cache': 'no-cache',
        'Content-Type': 'text/html;charset=utf-8'
    };

    page.open(url,/*{ keepAlive: true },*/ function (s) {
        if (status=== "success" ) {
            page.evaluate(function () {
                $(".canvas_box").appendTo(".app_box").css("float","none").siblings().remove();
                $(".app_box,body").css("margin",0);
            });
            var args = require('system').args;
            var fs = require('fs');
			var page = new WebPage();
			if ( 1 === args.length ) {
                console.log('Url address is required');
            phantom.exit();
            }
			var url = args[1].toLowerCase();
			var ext = getFileExtension();
			var clipping = getClipping();
			var viewports = [
                {
                    width : 1200,
                    height : 800
                }
            ];
			var folder = urlToDir(urlAddress);
			var output, key;
			function render(n) {
				if ( !!n ) {
					key = n - 1;
                    page.viewportSize = viewports[key];
                    if ( clipping ) {
                       page.clipRect = viewports[key];
                    }
                    output = folder + "/" + getFileName(viewports[key]);
                    console.log('Saving ' + output);
                    page.render(output);
					var base64= page.renderBase64(output),type="data:image/png;base64,"
					var img="<img src='"+type+base64+"'>"
					res.write(img);
					res.close();
                    render(key);
                          }
                    }

                    render(viewports.length);
                }
		    if (service) {
		        console.log('Web server running on port ' + port);
	     	} else {
		        console.log('Error: Could not create web server listening on port ' + port);
                phantom.exit();
	        }
		}
    });



function getFileName(viewport) {
    var d = new Date();
    var date = [
        d.getUTCFullYear(),
        d.getUTCMonth() + 1,
        d.getUTCDate()
    ];
    var time = [
        d.getHours() <= 9 ? '0' + d.getHours() : d.getHours(),
        d.getMinutes() <= 9 ? '0' + d.getMinutes() : d.getMinutes(),
        d.getSeconds() <= 9 ? '0' + d.getSeconds() : d.getSeconds(),
        d.getMilliseconds()
    ];
    var resolution = viewport.width + (clipping ? "x" + viewport.height : '');

    return date.join('-') + '_' + time.join('-') + "_" + resolution + ext;
}

/**
 * output extension format helper
 *
 * @returns {*}
 */
function getFileExtension() {
    if ( 'true' != args[2] && !!args[2] ) {
        return '.' + args[2];
    }
    return '.png';
}

/**
 * check if clipping
 *
 * @returns {boolean}
 */
function getClipping() {
    if ( 'true' == args[3] ) {
        return !!args[3];
    } else if ( 'true' == args[2] ) {
        return !!args[2];
    }
    return false;
}

/**
 * url to directory helper
 *
 * @param url
 * @returns {string}
 */
function urlToDir(url) {
    var dir = url
        .replace(/^(http|https):\/\//, '')
        .replace(/\/$/, '');

    if ( !fs.makeTree(dir) ) {
        console.log('"' + dir + '" is NOT created.');
        phantom.exit();
    }
    return dir;
}



