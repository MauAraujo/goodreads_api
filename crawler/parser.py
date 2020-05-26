import html2text
from lexico import *

class Parser():
    def __init__(self):
        self.parser = html2text.HTML2Text()
        self.parser.ignore_links = True

    def parse_html(self, html):
        return self.parser.handle(html)

    def parse_html_tokens_to_string(self, html):
        tokens = self.parse_html_tokens(html)
        tokens_string = ''
        for token in tokens:
            tokens_string += str(token)
        return tokens_string    

        
    def parse_html_tokens(self, html):
        text = self.parser.handle(html)
        return get_user_tokens(text)

def main():
    parser = Parser()
    print(parser.parse_html_tokens_to_string("""
	
	
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8"/>

            <title>20 comidas sanas que se preparan en 15 minutos</title>
        <meta name="description" content="Tener poco tiempo para cocinar no está reñido con comer sano. Un ejemplo son estas 20 comidas sanas que harás en poco tiempo."/>
        <link rel="canonical" href="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102.html" />
        <meta property="og:title" content="20 comidas sanas que se preparan en 15 minutos"/>
        <meta property="og:url" content="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102.html"/>
        <meta property="og:description" content="Tener poco tiempo para cocinar no está reñido con comer sano. Un ejemplo son estas 20 comidas sanas que harás en poco tiempo."/>
        <meta property="og:image" content="https://www.objetivobienestar.com/uploads/s1/58/75/42/istock-93400103-medium-3-360x213.jpeg"/>
        <meta property="og:image:width" content="360" />
        <meta property="og:image:height" content="213" />
        <meta property="og:type" content="website"/>
    
        <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:url" content="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102.html"/>
    <meta name="twitter:description" content="Tener poco tiempo para cocinar no está reñido con comer sano. Un ejemplo son estas 20 comidas sanas que harás en poco tiempo."/>
    <meta name="twitter:image:src" content="https://www.objetivobienestar.com/uploads/s1/58/75/42/istock-93400103-medium-3-360x213.jpeg"/>
            <meta property="article:modified_time" content="" />
    <link rel="amphtml" href="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102_amp.html"/>

	<meta property="fb:pages" content="597953056942918" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, maximum-scale=1" />

    <link rel="shortcut icon" type="image/png" href="/favicon.png?v=2"/>
    <link rel="apple-touch-icon" href="//www.objetivobienestar.com/uploads/static/apple-touch-icon.png">
    <link rel="icon" type="image/png" href="//www.objetivobienestar.com/uploads/static/favicon-16x16.png" sizes="16x16">
    <link rel="icon" type="image/png" href="//www.objetivobienestar.com/uploads/static/android-chrome-192x192.png" sizes="192x192">

    
    
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    
    <!-- Icons
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"> -->

        
    <meta name="robots" content="index,follow">

    <!-- Site Microdata -->
    <script data-schema="Organization" type="application/ld+json">{"name":"Editorial Planeta, S.A.U.", "url":"https://www.objetivobienestar.com","logo":"https://www.objetivobienestar.com/apple-touch-icon-152x152.png","sameAs":["https://www.facebook.com/objetivobienestar","https://twitter.com/obienestar","https://plus.google.com/+Objetivobienestar/posts","https://www.pinterest.com/obienestar/"],"@type":"Organization","@context":"http://schema.org"} </script>
    
            <!-- Google Analytics -->
        <script>
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
            ga('create', 'UA-48315418-1', 'auto');
            ga('send', 'pageview');
        </script>
        
    
    <script async='async' src='https://www.googletagservices.com/tag/js/gpt.js'></script>
    <script>
        var gptadslots = [];
        var googletag = googletag || {cmd:[]};
    </script>
    <script>
        googletag.cmd.push(function() {
                                        
            var mapping1 = googletag.sizeMapping()
                .addSize([728, 250], [[728, 90], [970, 90], [980, 90], [970, 250], [980, 250], 'fluid'])
                .addSize([0, 0], [[320, 50], [320, 100], [234, 60], 'fluid'])
                .build();

            gptadslots.push(googletag.defineOutOfPageSlot('/21784895357/objetivobienestar/alimentacion-saludable-noticias-float', 'div-gpt-ad-float')
                .setTargeting('pos', ['float'])
                .addService(googletag.pubads()));

            gptadslots.push(googletag.defineSlot('/21784895357/objetivobienestar/alimentacion-saludable-noticias-ldb1', 'fluid', 'div-gpt-ad-ldb1')
                .setTargeting('pos', ['ldb1'])
                .setTargeting('place', ['atf'])
                .defineSizeMapping(mapping1)
                .addService(googletag.pubads()));

            gptadslots.push(googletag.defineSlot('/21784895357/objetivobienestar/alimentacion-saludable-noticias-mpu1', ['fluid',[300,250],[300,600],[336,280]], 'div-gpt-ad-mpu1')
                .setTargeting('pos', ['mpu1'])
                .setTargeting('place', ['atf'])
                .addService(googletag.pubads()));

            gptadslots.push(googletag.defineSlot('/21784895357/objetivobienestar/alimentacion-saludable-noticias-ldb2', 'fluid', 'div-gpt-ad-ldb2')
                .setTargeting('pos', ['ldb2'])
                .setTargeting('place', ['btf'])
                .defineSizeMapping(mapping1)
                .addService(googletag.pubads()));

            gptadslots.push(googletag.defineSlot('/21784895357/objetivobienestar/alimentacion-saludable-noticias-ldb3', 'fluid', 'div-gpt-ad-ldb3')
                .setTargeting('pos', ['ldb3'])
                .setTargeting('place', ['btf'])
                .defineSizeMapping(mapping1)
                .addService(googletag.pubads()));

            gptadslots.push(googletag.defineSlot('/21784895357/objetivobienestar/alimentacion-saludable-noticias-mpu2', [[300,250],[336,250]], 'div-gpt-ad-mpu2')
                .setTargeting('pos', ['mpu2'])
                .setTargeting('place', ['btf'])
                .addService(googletag.pubads()));

                            gptadslots.push(googletag.defineSlot('/21784895357/objetivobienestar/alimentacion-saludable-noticias-mpu3', ['fluid',[300,250],[300,600],[336,280]], 'div-gpt-ad-mpu3')
                    .setTargeting('pos', ['mpu3'])
                    .setTargeting('place', ['atf'])
                    .addService(googletag.pubads()));
            
                        googletag.pubads().collapseEmptyDivs();
                            googletag.pubads().setTargeting('section', 'noticias');
                        googletag.enableServices();
        });
    </script>

    <script src="https://s3.eu-central-1.amazonaws.com/sc-devel/Skins/SMCService.js" async></script>
    <!-- Begin comScore Tag -->
    <script>
      var _comscore = _comscore || [];
      _comscore.push({ c1: "2", c2: "22656911" });
      (function() {
        var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
        s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
        el.parentNode.insertBefore(s, el);
      })();
    </script>
    <noscript>
      <img src="http://b.scorecardresearch.com/p?c1=2&c2=22656911&cv=2.0&cj=1" />
    </noscript>

    <!-- AddThis -->
    <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-5769632ad8c8421b"></script>
    
    <!-- Recaptcha -->
    <script src="https://www.google.com/recaptcha/api.js?hl=es" async defer></script>
    
    <script type="text/javascript" src="//www.objetivobienestar.com/uploads/static/objetivobienestar/digitalData.js"></script>
    <script type="text/javascript" src="//assets.adobedtm.com/f8735ec9fc76f6b0820878a4989891bbd6063199/satelliteLib-88eb3c99d783eae9d7e08234317da6028e80b161.js"></script>
    <script type="text/javascript">
                    jQuery(function ($) {
            	var values, params = [];
            	var fields = [
            		'utm_medium', 'utm_source', 'utm_publisher',
            		'utm_campaign', 'utm_term', 'utm_term' /* FIXME */
            	];
            	var foundTags = true;
            
            	if (document.location.search) {
            		values = location.search.substr(1).split("&");
            		$.each(values, function(index, value){
            			var tmp = value.split("=");
            			if (tmp) {
            				params[ tmp[0] ] = (
            					typeof(tmp[1]) != "undefined" ? tmp[1] : ''
            				);
            			}
            		});
            	}
            
            	$.each(fields, function(index, field){
            		if (typeof(params[field]) == "undefined") {
            			value = getCookie(field);
            			if (value !== false) {
            				params[field] = value;
            			} else {
            				foundTags = false;
            			}
            		}
            
            		return foundTags;
            	});
            	if (typeof(params['c']) != "undefined") {
            		$.each(fields, function(index, field){
                		if (typeof(params[field]) == "undefined") {
                			params[field] = '';
                		}
                	});
            		params['utm_campaign'] = params['c'];
            		foundTags = true;
                }
            
            	if (foundTags) {
            		dataLayer.setCampaign (
            			params['utm_medium'], params['utm_source'], params['utm_publisher'],
            			params['utm_campaign'], params['utm_term'], params['utm_term']
            		);
            		$.each(fields, function(index, field){
                		setCookie(field, params[field], 0);
            		});
            	}
            
                function setCookie(name, value, lifetime)
                {
                    var date = new Date();
            
                	if (lifetime >= 0) {
                        date.setTime(
                            date.getTime()+(lifetime*1000)
                        );
                        document.cookie = name+'='+escape(value)
                            +"; expires="+(
                            	lifetime > 0 ? date.toGMTString() : 0
                            )
                            +"; path=/";
                    }
                }
            
                function getCookie(name)
                {
                    var value = false;
                    var ca = document.cookie.split(';');
            
                    name += "=";
                    for (var i = 0; (i < ca.length && !value); i++) {
                        var c = ca[i];
            
                        while (c.charAt(0) == ' ') {
                            c = c.substring(1);
                        }
                        if (c.indexOf(name) != -1) {
                            value = decodeURIComponent(
                            	c.substring(
            	                    name.length, c.length
            	                )
            	            );
                        }
                    }
            
                    return value;
                }
            });
            </script>
    
        
    <!-- Taboola -->
    <script type="text/javascript">
        window._taboola = window._taboola || [];
        _taboola.push({article:'auto'});
        !function (e, f, u, i) {
            if (!document.getElementById(i)){
                e.async = 1;
                e.src = u;
                e.id = i;
                f.parentNode.insertBefore(e, f);
            }
        }(document.createElement('script'),
            document.getElementsByTagName('script')[0],
            '//cdn.taboola.com/libtrc/prismapublicaciones-objetivobienestar/loader.js',
            'tb_loader_script');
        if(window.performance && typeof window.performance.mark == 'function')
        {window.performance.mark('tbl_ic');}
    </script>
    
    <!-- Quantcast Choice. Consent Manager Tag -->
    <script type="text/javascript" async=true>
        var elem = document.createElement('script');
        elem.src = 'https://quantcast.mgr.consensu.org/cmp.js';
        elem.async = true;
        elem.type = "text/javascript";
        var scpt = document.getElementsByTagName('script')[0];
        scpt.parentNode.insertBefore(elem, scpt);
        (function() {
        var gdprAppliesGlobally = false;
        function addFrame() {
            if (!window.frames['__cmpLocator']) {
            if (document.body) {
                var body = document.body,
                    iframe = document.createElement('iframe');
                iframe.style = 'display:none';
                iframe.name = '__cmpLocator';
                body.appendChild(iframe);
            } else {
                // In the case where this stub is located in the head,
                // this allows us to inject the iframe more quickly than
                // relying on DOMContentLoaded or other events.
                setTimeout(addFrame, 5);
            }
            }
        }
        addFrame();
        function cmpMsgHandler(event) {
            var msgIsString = typeof event.data === "string";
            var json;
            if(msgIsString) {
            json = event.data.indexOf("__cmpCall") != -1 ? JSON.parse(event.data) : {};
            } else {
            json = event.data;
            }
            if (json.__cmpCall) {
            var i = json.__cmpCall;
            window.__cmp(i.command, i.parameter, function(retValue, success) {
                var returnMsg = {"__cmpReturn": {
                "returnValue": retValue,
                "success": success,
                "callId": i.callId
                }};
                event.source.postMessage(msgIsString ?
                JSON.stringify(returnMsg) : returnMsg, '*');
            });
            }
        }
        window.__cmp = function (c) {
            var b = arguments;
            if (!b.length) {
            return __cmp.a;
            }
            else if (b[0] === 'ping') {
            b[2]({"gdprAppliesGlobally": gdprAppliesGlobally,
                "cmpLoaded": false}, true);
            } else if (c == '__cmp')
            return false;
            else {
            if (typeof __cmp.a === 'undefined') {
                __cmp.a = [];
            }
            __cmp.a.push([].slice.apply(b));
            }
        }
        window.__cmp.gdprAppliesGlobally = gdprAppliesGlobally;
        window.__cmp.msgHandler = cmpMsgHandler;
        if (window.addEventListener) {
            window.addEventListener('message', cmpMsgHandler, false);
        }
        else {
            window.attachEvent('onmessage', cmpMsgHandler);
        }
        })();
        window.__cmp('init', {
        		'Language': 'es',
    		'Initial Screen Title Text': 'Tu privacidad es importante para nosotros',
    		'Initial Screen Reject Button Text': 'NO ACEPTO',
    		'Initial Screen Accept Button Text': 'ACEPTO',
    		'Initial Screen Purpose Link Text': 'Mostrar objetivos',
    		'Purpose Screen Title Text': 'Tu privacidad es importante para nosotros',
    		'Purpose Screen Body Text': 'Puede establecer sus preferencias de consentimiento y determinar cómo desea que se utilicen sus datos según los fines que se detallan a continuación. Puede establecer sus preferencias con respecto a nosotros independientemente de las de los socios externos. Cada objetivo tiene una descripción para que sepa cómo nosotros y los socios usamos sus datos.',
    		'Purpose Screen Vendor Link Text': 'Visualizza i fornitori',
    		'Purpose Screen Cancel Button Text': 'Cancelar',
    		'Purpose Screen Save and Exit Button Text': 'Guardar y salir',
    		'Vendor Screen Title Text': 'Tu privacidad es importante para nosotros',
    		'Vendor Screen Body Text': 'Puede configurar las preferencias de consentimiento para los terceros externos individuales con los que trabajamos a continuación. Expanda cada elemento de la lista de la compañía para ver para qué fines usan los datos para ayudarlo a tomar sus decisiones. En algunos casos, las compañías pueden usar sus datos sin pedir su consentimiento en función de sus intereses legítimos. Puede hacer clic en los enlaces de sus políticas de privacidad para obtener más información y para objetar dicho procesamiento.',
    		'Vendor Screen Accept All Button Text': 'ACEPTAR TODO',
    		'Vendor Screen Reject All Button Text': 'RECHAZAR TODO',
    		'Vendor Screen Purposes Link Text': 'Volver a los propósitos',
    		'Vendor Screen Cancel Button Text': 'Cancelar',
    		'Vendor Screen Save and Exit Button Text': 'Guardar y salir',
    		'Initial Screen Body Text': 'Nosotros y nuestros socios utilizamos tecnologías, como las cookies, y procesamos datos personales, como las direcciones IP y los identificadores de cookies, para personalizar los anuncios y el contenido según sus intereses, medir el rendimiento de los anuncios y el contenido y obtener información sobre las audiencias que vieron los anuncios y el contenido. Haga clic a continuación para autorizar el uso de esta tecnología y el procesamiento de sus datos personales para estos fines. Puede cambiar de opinión y cambiar sus opciones de consentimiento en cualquier momento al regresar a este sitio.',
    		'Initial Screen Body Text Option': 1,
    		'Publisher Name': 'Objetivo Bienestar',
    		'Publisher Logo': 'https://www.objetivobienestar.com/uploads/static/objetivobienestar/logo_header.png',
    		'Publisher Purpose IDs': [1,2,3,4,5],
    		'Post Consent Page': 'https://www.objetivobienestar.com/politica-de-privacidad.html',
    		'Consent Scope': 'service',
    		'UI Layout': 'banner',
        });
    </script>
    <!-- End Quantcast Choice. Consent Manager Tag -->
		
	<link rel="stylesheet" href="/css/2edea00.css?v=5ebe8dec74b67" />

<link rel="stylesheet" href="/css/b6b0f9e.css?v=5ebe8dec91439" />	</head>

<body itemscope itemtype="http://schema.org/WebPage"     class="article category-3">

    <!-- Google Tag Manager -->
    <noscript>
        <iframe src="//www.googletagmanager.com/ns.html?id=GTM-T7K5MN" height="0" width="0" style="display:none;visibility:hidden"></iframe>
    </noscript>
    
    <script>
        (function (w, d, s, l, i) {
            w[l] = w[l] || [];
            w[l].push(
                {'gtm.start': new Date().getTime(), event: 'gtm.js'}
            );
            var f = d.getElementsByTagName(s)[0],
                j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
            j.async = true;
            j.src = '//www.googletagmanager.com/gtm.js?id=' + i + dl;
            f.parentNode.insertBefore(j, f);
        })(window, document, 'script', 'dataLayer2', 'GTM-T7K5MN');
    </script>
    
    <div class="page">
        <div class="cscontent">
                <div class="row row-top">
        <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6"><div class="csl-inner csl-hot">

    <header>
        <div class="top-banner">
                    </div>
        <div class="wrapper">
            <span data-role="mobile-menu-button" class="btn-nav" title="Menú"></span>
            <div class="logo">
                <a href="/" title="Objetivo Bienestar"></a>
            </div>
            <div class="nav-reduced"></div>
        </div>
        <div class="nav-desktop">
            <div class="wrapper">

                <nav data-role="menu-items">
                    <ul>
                                                    <li class="sub">
                                <a href="https://www.objetivobienestar.com/alimentacion-saludable" title="Alimentación">Alimentación</a>
                                <ul class="sub">
                                    <li>
                                                                                    <ul>
                                                                                                    <li><a href="https://www.objetivobienestar.com/menu-semanal-saludable_115_119.html" title="Menú semanal saludable">Menú semanal saludable</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/recetas-veganas_54_119.html" title="Recetas veganas">Recetas veganas</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/comer-sano_39_119.html" title="Comer sano">Comer sano</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/desayunos_40_119.html" title="Desayunos">Desayunos</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/superalimentos_25_119.html" title="Superalimentos">Superalimentos</a></li>
                                                                                            </ul>
                                        
                                        <div class="news">
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/veganismo-la-cultura-hegemonica-del-futuro_42253_102.html" title="Veganismo, la cultura hegemónica del futuro">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/76/94/veganismo-la-cultura-hegemonica-del-futuro_3_360x213.jpeg" title="Veganismo, la cultura hegemónica del futuro" alt="Veganismo, la cultura hegemónica del futuro" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/76/94/veganismo-la-cultura-hegemonica-del-futuro_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/76/91/veganismo-la-cultura-hegemonica-del-futuro.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/veganismo-la-cultura-hegemonica-del-futuro_42253_102.html" title="Veganismo, la cultura hegemónica del futuro">Veganismo, la cultura hegemónica del futuro</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/receta-ensalada-thai_42229_102.html" title="Ensalada thai">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/53/07/receta-ensalda-thai_3_360x213.jpeg" title="Receta Ensalda thai" alt="Receta Ensalda thai" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/53/07/receta-ensalda-thai_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/53/04/receta-ensalda-thai.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/receta-ensalada-thai_42229_102.html" title="Ensalada thai">Ensalada thai</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/receta-delicioso-brownie-vegano-solo-tres-ingredientes_42228_102.html" title="El delicioso brownie vegano de solo tres ingredientes">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/52/81/el-delicioso-brownie-vegano-de-solo-tres-ingredientes_3_360x213.jpeg" title="El delicioso brownie vegano de solo tres ingredientes" alt="El delicioso brownie vegano de solo tres ingredientes" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/52/81/el-delicioso-brownie-vegano-de-solo-tres-ingredientes_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/52/78/el-delicioso-brownie-vegano-de-solo-tres-ingredientes.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/receta-delicioso-brownie-vegano-solo-tres-ingredientes_42228_102.html" title="El delicioso brownie vegano de solo tres ingredientes">El delicioso brownie vegano de solo tres ingredientes</a>
                                                    </h2>
                                                </div>
                                                                                    </div>
                                    </li>
                                </ul>
                            </li>
                                                    <li class="sub">
                                <a href="https://www.objetivobienestar.com/habitos-de-vida-saludable" title="Salud">Salud</a>
                                <ul class="sub">
                                    <li>
                                                                                    <ul>
                                                                                                    <li><a href="https://www.objetivobienestar.com/salud-intestinal_63_119.html" title="Salud intestinal">Salud intestinal</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/habitos-saludables_22_119.html" title="Hábitos saludables">Hábitos saludables</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/dejar-de-fumar_27_119.html" title="Dejar de fumar">Dejar de fumar</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/dolor-de-espalda_43_119.html" title="Dolor de espalda">Dolor de espalda</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/diabetes_42_119.html" title="Diabetes">Diabetes</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/trucos-para-dormir_60_119.html" title="Trucos para dormir">Trucos para dormir</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/salud-femenina_56_119.html" title="Salud femenina">Salud femenina</a></li>
                                                                                            </ul>
                                        
                                        <div class="news">
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/que-diferencia-hay-entre-alergia-intolerancia-alimentaria_42206_102.html" title="¿Qué diferencia hay entre una alergia y una intolerancia alimentaria?">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/36/51/que-diferencia-hay-entre-una-alergia-y-una-intolerancia-alimentaria_3_360x213.jpeg" title="Qué diferencia hay entre una alergia y una intolerancia alimentaria" alt="Qué diferencia hay entre una alergia y una intolerancia alimentaria" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/36/51/que-diferencia-hay-entre-una-alergia-y-una-intolerancia-alimentaria_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/36/48/que-diferencia-hay-entre-una-alergia-y-una-intolerancia-alimentaria.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/que-diferencia-hay-entre-alergia-intolerancia-alimentaria_42206_102.html" title="¿Qué diferencia hay entre una alergia y una intolerancia alimentaria?">¿Qué diferencia hay entre una alergia y una intolerancia alimentaria?</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/trastorno-por-deficit-naturaleza-que-es-como-evitarlo_42190_102.html" title="Trastorno por déficit de naturaleza: ¿qué es y cómo evitarlo?">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/22/46/trastorno-por-deficit-de-naturaleza-que-es-y-como-evitarlo_3_360x213.jpeg" title="Trastorno por déficit de naturaleza ¿qué es y cómo evitarlo" alt="Trastorno por déficit de naturaleza ¿qué es y cómo evitarlo" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/22/46/trastorno-por-deficit-de-naturaleza-que-es-y-como-evitarlo_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/22/43/trastorno-por-deficit-de-naturaleza-que-es-y-como-evitarlo.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/trastorno-por-deficit-naturaleza-que-es-como-evitarlo_42190_102.html" title="Trastorno por déficit de naturaleza: ¿qué es y cómo evitarlo?">Trastorno por déficit de naturaleza: ¿qué es y cómo evitarlo?</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/que-tener-en-cuenta-mejorar-calidad-ovarica-segun-medicina-tradicional-china_42180_102.html" title="¿Qué tener en cuenta para mejorar la calidad ovárica según la medicina tradicional china?">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/14/14/que-tener-en-cuenta-para-mejorar-la-calidad-ovarica-segun-la-medicina-tradicional-china_3_360x213.jpeg" title="Qué tener en cuenta para mejorar la calidad ovárica según la medicina tradicional china" alt="Qué tener en cuenta para mejorar la calidad ovárica según la medicina tradicional china" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/14/14/que-tener-en-cuenta-para-mejorar-la-calidad-ovarica-segun-la-medicina-tradicional-china_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/14/11/que-tener-en-cuenta-para-mejorar-la-calidad-ovarica-segun-la-medicina-tradicional-china.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/que-tener-en-cuenta-mejorar-calidad-ovarica-segun-medicina-tradicional-china_42180_102.html" title="¿Qué tener en cuenta para mejorar la calidad ovárica según la medicina tradicional china?">¿Qué tener en cuenta para mejorar la calidad ovárica según la medicina tradicional china?</a>
                                                    </h2>
                                                </div>
                                                                                    </div>
                                    </li>
                                </ul>
                            </li>
                                                    <li class="sub">
                                <a href="https://www.objetivobienestar.com/salud-mental" title="Mente">Mente</a>
                                <ul class="sub">
                                    <li>
                                                                                    <ul>
                                                                                                    <li><a href="https://www.objetivobienestar.com/ser-feliz_17_119.html" title="Ser feliz">Ser feliz</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/mindfulness_30_119.html" title="Mindfulness">Mindfulness</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/ansiedad_14_119.html" title="Ansiedad">Ansiedad</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/autoestima_18_119.html" title="Autoestima">Autoestima</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/meditacion_20_119.html" title="Meditación">Meditación</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/yoga-para-principiantes_15_119.html" title="Yoga">Yoga</a></li>
                                                                                            </ul>
                                        
                                        <div class="news">
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/la-trampa-de-la-positividad_42250_102.html" title="La trampa de la positividad">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/10/11/trampa-positividad.jpeg" title="La trampa de la positividad" alt="La trampa de la positividad" height="" width="" data-prosrcset="" data-original="https://www.objetivobienestar.com/uploads/s1/91/10/11/trampa-positividad.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/la-trampa-de-la-positividad_42250_102.html" title="La trampa de la positividad">La trampa de la positividad</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/7-formas-despedir-ser-querido-rituales-funerarios-mas-curiosos-planeta_42245_102.html" title="7 formas de despedir a un ser querido: los rituales funerarios más curiosos del planeta">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/67/72/7-formas-de-despedir-a-un-ser-querido_3_360x213.jpeg" title="7 formas de despedir a un ser querido" alt="7 formas de despedir a un ser querido" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/67/72/7-formas-de-despedir-a-un-ser-querido_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/67/69/7-formas-de-despedir-a-un-ser-querido.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/7-formas-despedir-ser-querido-rituales-funerarios-mas-curiosos-planeta_42245_102.html" title="7 formas de despedir a un ser querido: los rituales funerarios más curiosos del planeta">7 formas de despedir a un ser querido: los rituales funerarios más curiosos del planeta</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/sindrome-cabana-miedo-volver-nueva-normalidad_42231_102.html" title="El síndrome de la cabaña: el miedo a volver a la nueva normalidad">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/54/50/el-sindrome-de-la-cabana-el-miedo-a-volver-a-la-nueva-normalidad_3_360x213.jpeg" title="El síndrome de la cabaña el miedo a volver a la nueva normalidad" alt="El síndrome de la cabaña el miedo a volver a la nueva normalidad" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/54/50/el-sindrome-de-la-cabana-el-miedo-a-volver-a-la-nueva-normalidad_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/54/47/el-sindrome-de-la-cabana-el-miedo-a-volver-a-la-nueva-normalidad.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/sindrome-cabana-miedo-volver-nueva-normalidad_42231_102.html" title="El síndrome de la cabaña: el miedo a volver a la nueva normalidad">El síndrome de la cabaña: el miedo a volver a la nueva normalidad</a>
                                                    </h2>
                                                </div>
                                                                                    </div>
                                    </li>
                                </ul>
                            </li>
                                                    <li class="sub">
                                <a href="https://www.objetivobienestar.com/relaciones-de-pareja" title="Amor y sexo">Amor y sexo</a>
                                <ul class="sub">
                                    <li>
                                                                                    <ul>
                                                                                                    <li><a href="https://www.objetivobienestar.com/relaciones_12_119.html" title="Relaciones">Relaciones</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/orgasmo_50_119.html" title="Orgasmo">Orgasmo</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/autoestima_18_119.html" title="Autoestima">Autoestima</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/ser-feliz_17_119.html" title="Ser feliz">Ser feliz</a></li>
                                                                                            </ul>
                                        
                                        <div class="news">
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/pornografia-feminista-5-mitos-populares_41778_102.html" title="La pornografía feminista y sus 5 mitos más populares">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/39/10/la-pornografia-feminista-y-sus-5-mitos-mas-populares_3_360x213.jpeg" title="La pornografía feminista y sus 5 mitos más populares" alt="La pornografía feminista y sus 5 mitos más populares" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/39/10/la-pornografia-feminista-y-sus-5-mitos-mas-populares_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/39/07/la-pornografia-feminista-y-sus-5-mitos-mas-populares.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/pornografia-feminista-5-mitos-populares_41778_102.html" title="La pornografía feminista y sus 5 mitos más populares">La pornografía feminista y sus 5 mitos más populares</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/10-verdades-orgasmo-masculino_42138_102.html" title="Las 10 verdades del orgasmo masculino">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/90/55/05/las-10-verdades-del-orgasmo-masculino_3_360x213.jpeg" title="Las 10 verdades del orgasmo masculino" alt="Las 10 verdades del orgasmo masculino" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/90/55/05/las-10-verdades-del-orgasmo-masculino_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/90/55/02/las-10-verdades-del-orgasmo-masculino.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/10-verdades-orgasmo-masculino_42138_102.html" title="Las 10 verdades del orgasmo masculino">Las 10 verdades del orgasmo masculino</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/quien-fue-lili-elbe_42093_102.html" title="¿Quién fue Lili Elbe?">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/90/24/52/lili-chico_3_360x213.jpeg" title="¿Quién fue Lili Elbe?" alt="¿Quién fue Lili Elbe?" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/90/24/52/lili-chico_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/90/24/51/lili-chico.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/quien-fue-lili-elbe_42093_102.html" title="¿Quién fue Lili Elbe?">¿Quién fue Lili Elbe?</a>
                                                    </h2>
                                                </div>
                                                                                    </div>
                                    </li>
                                </ul>
                            </li>
                                                    <li class="sub">
                                <a href="https://www.objetivobienestar.com/consejos-de-belleza" title="Belleza">Belleza</a>
                                <ul class="sub">
                                    <li>
                                                                                    <ul>
                                                                                                    <li><a href="https://www.objetivobienestar.com/piel_4_119.html" title="Piel">Piel</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/masajes_45_119.html" title="Masajes">Masajes</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/pelo_51_119.html" title="Pelo">Pelo</a></li>
                                                                                            </ul>
                                        
                                        <div class="news">
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/formas-reducir-plasticos-en-geles-champus_42252_102.html" title="5 formas de reducir plásticos en geles y champús">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/76/81/5-formas-de-reducir-plasticos-en-geles-y-champus_3_360x213.jpeg" title="5 formas de reducir plásticos en geles y champús" alt="5 formas de reducir plásticos en geles y champús" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/76/81/5-formas-de-reducir-plasticos-en-geles-y-champus_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/76/78/5-formas-de-reducir-plasticos-en-geles-y-champus.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/formas-reducir-plasticos-en-geles-champus_42252_102.html" title="5 formas de reducir plásticos en geles y champús">5 formas de reducir plásticos en geles y champús</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/piezas-ropa-indispensables-tu-armario-mujer_42197_102.html" title="10 piezas de ropa indispensables para tu armario">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/29/26/10-piezas-de-ropa-indispensables-para-tu-armario_3_360x213.jpeg" title="10 piezas de ropa indispensables para tu armario " alt="10 piezas de ropa indispensables para tu armario " height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/29/26/10-piezas-de-ropa-indispensables-para-tu-armario_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/29/23/10-piezas-de-ropa-indispensables-para-tu-armario.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/piezas-ropa-indispensables-tu-armario-mujer_42197_102.html" title="10 piezas de ropa indispensables para tu armario">10 piezas de ropa indispensables para tu armario</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/movimientos-yoga-facial-expres-hacer-cada-dia-en-solo-minuto_42185_102.html" title="11 movimientos de yoga facial exprés para hacer cada día en solo un minuto">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/18/70/11-movimientos-de-yoga-facial-expres-para-hacer-cada-dia-en-solo-un-minuto_3_360x213.jpeg" title="11 movimientos de yoga facial exprés para hacer cada día en solo un minuto" alt="11 movimientos de yoga facial exprés para hacer cada día en solo un minuto" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/18/70/11-movimientos-de-yoga-facial-expres-para-hacer-cada-dia-en-solo-un-minuto_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/18/67/11-movimientos-de-yoga-facial-expres-para-hacer-cada-dia-en-solo-un-minuto.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/movimientos-yoga-facial-expres-hacer-cada-dia-en-solo-minuto_42185_102.html" title="11 movimientos de yoga facial exprés para hacer cada día en solo un minuto">11 movimientos de yoga facial exprés para hacer cada día en solo un minuto</a>
                                                    </h2>
                                                </div>
                                                                                    </div>
                                    </li>
                                </ul>
                            </li>
                                                    <li class="sub">
                                <a href="https://www.objetivobienestar.com/ponerse-en-forma" title="Gym">Gym</a>
                                <ul class="sub">
                                    <li>
                                                                                    <ul>
                                                                                                    <li><a href="https://www.objetivobienestar.com/rutinas-de-ejercicios_8_119.html" title="Rutinas de ejercicios">Rutinas de ejercicios</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/yoga-para-principiantes_15_119.html" title="Yoga">Yoga</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/running_16_119.html" title="Running">Running</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/ponte-en-forma_7_119.html" title="Ponte en forma">Ponte en forma</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/dolor-de-espalda_43_119.html" title="Dolor de espalda">Dolor de espalda</a></li>
                                                                                            </ul>
                                        
                                        <div class="news">
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/ejercicio-mejor-desayuno_41890_102.html" title="El ejercicio, ¿mejor hacerlo antes o después del desayuno?">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/88/68/66/el-ejercicio-mejor-antes-o-despues-del-desayuno_3_360x213.jpeg" title="El ejercicio mejor antes o después del desayuno" alt="El ejercicio mejor antes o después del desayuno" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/88/68/66/el-ejercicio-mejor-antes-o-despues-del-desayuno_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/88/68/63/el-ejercicio-mejor-antes-o-despues-del-desayuno.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/ejercicio-mejor-desayuno_41890_102.html" title="El ejercicio, ¿mejor hacerlo antes o después del desayuno?">El ejercicio, ¿mejor hacerlo antes o después del desayuno?</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/como-running-te-puede-ayudar-empoderarte_41930_102.html" title="Cómo el running puede ayudarte a empoderarte">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/48/15/running-para-empoderarte-las-claves-para-hacerlo-bien_3_360x213.jpeg" title="Running para empoderarte las claves para hacerlo bien" alt="Running para empoderarte las claves para hacerlo bien" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/48/15/running-para-empoderarte-las-claves-para-hacerlo-bien_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/48/12/running-para-empoderarte-las-claves-para-hacerlo-bien.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/como-running-te-puede-ayudar-empoderarte_41930_102.html" title="Cómo el running puede ayudarte a empoderarte">Cómo el running puede ayudarte a empoderarte</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/rutina-entrenamiento-funcional-full-body-todas-condiciones-fisicas_42215_102.html" title="Rutina de entrenamiento funcional full body para todas las condiciones físicas">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/41/24/rutina-de-entrenamiento-funcional-full-body-para-todas-las-condiciones-fisicas_3_360x213.jpeg" title="Rutina de entrenamiento funcional full body para todas las condiciones físicas" alt="Rutina de entrenamiento funcional full body para todas las condiciones físicas" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/41/24/rutina-de-entrenamiento-funcional-full-body-para-todas-las-condiciones-fisicas_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/41/21/rutina-de-entrenamiento-funcional-full-body-para-todas-las-condiciones-fisicas.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/rutina-entrenamiento-funcional-full-body-todas-condiciones-fisicas_42215_102.html" title="Rutina de entrenamiento funcional full body para todas las condiciones físicas">Rutina de entrenamiento funcional full body para todas las condiciones físicas</a>
                                                    </h2>
                                                </div>
                                                                                    </div>
                                    </li>
                                </ul>
                            </li>
                                                    <li class="sub">
                                <a href="https://www.objetivobienestar.com/ideas-para-vivir-mejor" title="Ideas">Ideas</a>
                                <ul class="sub">
                                    <li>
                                                                                    <ul>
                                                                                                    <li><a href="https://www.objetivobienestar.com/mandalas_3_119.html" title="Mandalas">Mandalas</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/ideas-de-decoracion_31_119.html" title="Ideas de decoración">Ideas de decoración</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/suenos_58_119.html" title="Sueños">Sueños</a></li>
                                                                                                    <li><a href="https://www.objetivobienestar.com/libros-para-ser-feliz_36_119.html" title="Libros para ser feliz">Libros para ser feliz</a></li>
                                                                                            </ul>
                                        
                                        <div class="news">
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/como-afecta-industria-moda-nuestro-bienestar_42238_102.html" title="¿Cómo afecta la industria de la moda a nuestro bienestar?">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/59/36/como-afecta-la-industria-de-la-moda-a-nuestro-bienesta_3_360x213.jpeg" title="Cómo afecta la industria de la moda a nuestro bienesta" alt="Cómo afecta la industria de la moda a nuestro bienesta" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/59/36/como-afecta-la-industria-de-la-moda-a-nuestro-bienesta_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/59/33/como-afecta-la-industria-de-la-moda-a-nuestro-bienesta.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/como-afecta-industria-moda-nuestro-bienestar_42238_102.html" title="¿Cómo afecta la industria de la moda a nuestro bienestar?">¿Cómo afecta la industria de la moda a nuestro bienestar?</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/como-cultivar-tu-propio-aloe-vera-sacarle-maximo-partido_42230_102.html" title="Cómo cultivar tu propio aloe vera y sacarle el máximo partido">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/54/37/como-cultivar-tu-propio-aloe-vera-y-sacarle-el-maximo-partido_3_360x213.jpeg" title="Cómo cultivar tu propio aloe vera y sacarle el máximo partido" alt="Cómo cultivar tu propio aloe vera y sacarle el máximo partido" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/54/37/como-cultivar-tu-propio-aloe-vera-y-sacarle-el-maximo-partido_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/54/34/como-cultivar-tu-propio-aloe-vera-y-sacarle-el-maximo-partido.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/como-cultivar-tu-propio-aloe-vera-sacarle-maximo-partido_42230_102.html" title="Cómo cultivar tu propio aloe vera y sacarle el máximo partido">Cómo cultivar tu propio aloe vera y sacarle el máximo partido</a>
                                                    </h2>
                                                </div>
                                                                                            <div class="item">
                                                    <a href="https://www.objetivobienestar.com/videojuegos-confinamiento-buen-equipo_42223_102.html" title="Videojuegos y confinamiento: un buen equipo">
                                                                                                                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/52/94/videojuegos-y-confinamiento-un-buen-equipo_3_360x213.jpeg" title="Videojuegos y confinamiento un buen equipo" alt="Videojuegos y confinamiento un buen equipo" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/52/94/videojuegos-y-confinamiento-un-buen-equipo_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/52/91/videojuegos-y-confinamiento-un-buen-equipo.jpeg" class="cs-responsive-image">
                                                                                                            </a>
                                                    <h2 class="title">
                                                        <a href="https://www.objetivobienestar.com/videojuegos-confinamiento-buen-equipo_42223_102.html" title="Videojuegos y confinamiento: un buen equipo">Videojuegos y confinamiento: un buen equipo</a>
                                                    </h2>
                                                </div>
                                                                                    </div>
                                    </li>
                                </ul>
                            </li>
                                            </ul>
                </nav>

                <div class="search">
                    <span data-role="mobile-search-button" class="btn-search" title="Buscador"></span>
                    <form data-role="search-form" action="https://www.objetivobienestar.com/buscador.html" method="get">
                        <input type="text" name="search" id="search" placeholder="Buscar..." />
                    </form>
                </div>

                
            </div>
        </div>
            </header>

</div></div>
    </div>
    <div class="wrapper">
        <div class="row row-content">
            <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6"><div class="csl-inner csl-hot"><div class="banner f4 v1" data-zonename="ldb1" >
    
        <div id="div-gpt-ad-ldb1">
        <script>
            if (typeof googletag !== "undefined") {
                googletag.cmd.push(function () {
                    googletag.display('div-gpt-ad-ldb1');
                });
            }
        </script>
    </div>
    
</div></div></div>
        </div>
        <div class="row row-content">    
            <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6"><div class="csl-inner"><div class="row editable_item">
<div class="col-xs-6 col-sm-6 col-md-4 col-lg-4 article-left"><div class="csl-inner csl-hot">

                    <script data-schema="NewsArticle" type="application/ld+json">{"@type":"NewsArticle","@context":"http:\/\/schema.org","mainEntityOfPage":{"@type":"WebPage","@id":"https:\/\/www.objetivobienestar.com\/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102.html"},"headline":"20 comidas sanas que se preparan en 15 minutos","image":{"@type":"ImageObject","url":"https:\/\/www.objetivobienestar.com\/uploads\/s1\/32\/57\/22\/iStock_93400103_MEDIUM.jpg","width":1697,"height":1131},"datePublished":"2019-05-06T13:28:00+0200","dateModified":"2019-05-06T13:31:55+0200","author":{"@type":"Person","name":"Objetivo Bienestar"},"publisher":{"@type":"Organization","name":"Objetivo Bienestar","logo":{"@type":"ImageObject","url":"http:\/\/www.objetivobienestar.com\/uploads\/static\/logo.jpg","width":"80","height":"325"}},"description":"Con la llegada de la primavera, apetecen comidas ligeras\u00a0y frescas.\u00a0Para ello, existen una infinidad de recetas saludables y variadas que puedes preparar r\u00e1pidamente para mentener una dieta equilibrada y deliciosa.\r\n\r\nDisfrutar comiendo deber\u00eda ser una obligaci\u00f3n, por eso, queremos que intentes mejorar la manera en la que nutres tu cuerpo para que tenga toda la energ\u00eda necesaria y para que no te aburras ni comiendo ni cocinando. Cuantos m\u00e1s alimentos y productos te gusten, m\u00e1s variedad de platos podr\u00e1s cocinar, pero a\u00fan que seas una de esas personas a las que no les gusta a penas nada, puedes encontrar la manera de adaptar los platos y recetas seg\u00fan tus especiales gustos.        \r\n\r\nTe proponemos 20 recetas sencillas de comidas sanas y f\u00e1ciles, para comer o cenar, que podr\u00e1s preparar aunque en tu rutina reine la queja \u201ca mi d\u00eda le faltan horas\u201d. Desde pasta con diferentes salsas o guarniciones, pasando por pescado o pollo y hasta deliciosas ensaladas que nada tienen que ver con las t\u00edpicas tan aburridas de lechuga y tomate.\r\n\r\nEs importante, para preparar platos saludables, que uses los productos de temporada seg\u00fan la \u00e9poca del a\u00f1o. Eso, no solo har\u00e1 que las recetas sean mucho m\u00e1s econ\u00f3micas, sin\u00f3 que tambi\u00e9n estar\u00e1n mucho m\u00e1s sabrosas. Lo mejor de estas 20 ideas que te proponemos es que, tambi\u00e9n te las puedes llevar en t\u00e1per a la oficina o al trabajo, incluso puedes hacer m\u00e1s cantidad y repetir a lo largo de la semana.\r\n\r\n\u00bfTe apetece probar alguna?\r\n\r\n\n                                                                                \n                    \n                        \n                            \n                            \n                                \n                                \n                                    1\/20\n                                \n\n                                                                    Ensalada de br\u00f3coli, zanahoria y nueces\n                                \n                                                                    Corta el br&oacute;coli en ramilletes y cu&eacute;celo en una cazuela con agua y sal durante 5 minutos. Esc&uacute;rrelo y res&eacute;rvalo. Pela las zanahoria, r&aacute;yalas y a&ntilde;&aacute;delas al br&oacute;coli. Prepara, en un vaso, una vinagreta con aceite y zumo de lim&oacute;n para aderezar la ensalada. Por &uacute;ltimo, pica un pu&ntilde;ado de nueces e incorp&oacute;ralas al plato.&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    2\/20\n                                \n\n                                                                    Espaguetis con revuelto de setas y gambas\n                                \n                                                                    Hierve los espaguetis en una cazuela. Por otro lado, pon a calentar una sart&eacute;n con aceite. Dora un ajo laminado. Agrega las setas (que deber&aacute;s lavar y escurrir antes) y salt&eacute;alas durante 10 minutos. A&ntilde;ade las gambas peladas y salt&eacute;alas. Incorpora los huevos batidos. Para que el aspecto sea el de un revoltillo y no el de una tortilla a la francesa, tienes que ir retirando la sart&eacute;n del fuego e ir removiendo la mezcla para cuajar bien el huevo.&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    3\/20\n                                \n\n                                                                    Ensalada de lentejas con calabaza, hummus y almendra\n                                \n                                                                    Escurre un bote de lentejas, p&aacute;sales un agua y res&eacute;rvalas en un bol. Corta y cuece la calabaza y m&eacute;zclala con las lentejas. Pica un pu&ntilde;ado de almendras y a&ntilde;&aacute;delas. Al&iacute;&ntilde;ala con sal y aceite de oliva virgen. Aparte, prepara el hummus. Una vez tenga la textura deseada, a&ntilde;ade unas cucharadas por encima a la ensalada.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                                                                                                                                                \n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    4\/20\n                                \n\n                                                                    Caldo de verduras r\u00e1pido\n                                \n                                                                    Limpia y pela verduras variadas como el apio, la zanahoria, el puerro o el nabo y c&oacute;rtalas a trocitos. Rehoga en una cazuela con un chorrito de aceite la cebolla y el puerro hasta que se doren. A&ntilde;ade el resto de verduras y salt&eacute;alas durante 5 minutos. Incorpora agua y hierbas arom&aacute;ticas como el tomillo y el laurel. Cu&eacute;celo todo a fuego suave durante 15 minutos. Cuendo est&eacute; listo, cu&eacute;lalo.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    5\/20\n                                \n\n                                                                    Cusc\u00fas con pollo, verduras y c\u00farcuma\n                                \n                                                                    Saltea una cebolla bien picada en la sart&eacute;n hasta que est&eacute; dorada. A&ntilde;ade pimiento verde, calabac&iacute;n y una pechuga de pollo troceada. Reh&oacute;galo todo durante 15 minutos. Por otro lado, lleva a ebullici&oacute;n 250 ml de agua con un chorrito de aceite y sal. Cuando el agua hierva, retira el recipiente del fuego y vierte 250 g de cusc&uacute;s. Remu&eacute;velo y d&eacute;jalo reposar 3 minutos. A&ntilde;ade una cucharada peque&ntilde;a de mantequilla y coloca de nuevo el recipiente en el fuego a baja temperatura durante 2-3 minutos, remueve el cusc&uacute;s con un tenedor. Incorpora el pollo y las verduras salteadas al cusc&uacute;s y sazona el plato con una cucharadita de c&uacute;rcuma.&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    6\/20\n                                \n\n                                                                    Espaguetis con espinacas, taquitos de jam\u00f3n y ajos tiernos\n                                \n                                                                    Cuece por un lado las espinacas y por otro la pasta. Saltea, en una sart&eacute;n con aceite, los ajos tiernos previamente lavados y cortados a trozos peque&ntilde;os. Para terminar, a&ntilde;ade unos tacos de jam&oacute;n serrano y reh&oacute;galos en la sart&eacute;n. Incorpora las espinacas y los espaguetis para mezclar todos los ingredientes.\r\n\r\n&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                                                                                                                                                \n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    7\/20\n                                \n\n                                                                    Lentejas con salm\u00f3n, eneldo y comino\n                                \n                                                                    Enjuaga las lentejas y res&eacute;rvalas. Pela y corta una cebolla a trozos peque&ntilde;os. Calienta una cazuela con aceite y dora las verduras y un ajo. Salpim&eacute;ntalo hasta que este pochado. A&ntilde;ade a las verduras comino y eneldo y c&uacute;brelas de caldo de pescado o de agua y cu&eacute;celo todo durante 4 minutos. Despu&eacute;s, cocina el salm&oacute;n 3 minutos por la parte de abajo y unos segundos por encima. Cuando est&eacute; listo, montamos una base con las lentejas y las verduras y colocamos encima el salm&oacute;n.&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    8\/20\n                                \n\n                                                                    Ensalada de calabaza con aguacate, tomate y pepino\n                                \n                                                                    Lava y pela las verduras. Raya muy fina la calabaza y trocea el aguacate, el tomate y el pepino en dados peque&ntilde;os. Para el aderezo final, usa aceite de oliva virgen extra, zumo de lim&oacute;n, salsa de soja y s&eacute;samo crudo.&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    9\/20\n                                \n\n                                                                    Escarola con pera y pasas\n                                \n                                                                    Lava la escarola, troc&eacute;ala y col&oacute;cala en una fuente. Agrega la pera cortada en dados, las pasas y pipas de girasol. Prepara un aderezo con sal, aceite de oliva y vinagre blanco de manzana.\r\n\r\n&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                                                                                                                                                \n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    10\/20\n                                \n\n                                                                    Jud\u00edas verdes con picada de ajo\n                                \n                                                                    Tan sencillo como jud&iacute;as verdes y ajo previamente dorado en la sart&eacute;n. El ajo le dar&aacute; un sabor diferente a el t&iacute;pico plato de verdura.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    11\/20\n                                \n\n                                                                    Aguacates rellenos de atu\u0301n\n                                \n                                                                    Necesitas aguacate, latas de at&uacute;n en aceite, pimiento escalivado y mayonesa. La elaboraci&oacute;n es muy sencilla ya que, solo hay que&nbsp;cortar por la mitad los aguacates y vaciarlos. Mezclar todos los ingredientes y usar la mezcla para volver a rellenar el aguacate. Lo mejor de esta receta es que puedes incorporar o eliminar cualquier producto seg&uacute;n tus gustos.&nbsp;\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    12\/20\n                                \n\n                                                                    Tortilla de espinacas\n                                \n                                                                    Todo el mundo sabe como hacer una trotilla. Para esta necesitas huevos y espinacas. Lo primero es batir el huevo, salpimentarlo y mientras tanto, por otro lado, hay que ir&nbsp;haciendo las espinacas con un poco de aceite. El resto ya es conocido: se junta todo y &iexcl;a la sart&eacute;n! hasta que est&eacute; hecha. Puedes a&ntilde;adirle patata, cebolla o cualquier otro vegetal que te guste.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                                                                                                                                                \n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    13\/20\n                                \n\n                                                                    Guisantes con jamo\u0301n\n                                \n                                                                    Saltear los guisantes con daditos o tiras finas de jam&oacute;n y &iexcl;listo! Tambi&eacute;n puedes a&ntilde;adirle al salteado cebolla para darle m&aacute;s textura y otro sabor. Tan sencillo y f&aacute;cil de preparar que la har&aacute;s en grandes cantidades para aprovecharla en otras comidas a lo largo de la&nbsp;semana.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    14\/20\n                                \n\n                                                                    Ensalada fri\u0301a de garbanzos\n                                \n                                                                    Para preparar esta ensalada a base de legumbres necesitas un bote de garbanzos cocidos, pimiento rojo y verde, cebolla, tomatitos cherry, olivas negras y ma&iacute;z. Aunque puedes a&ntilde;adirle cualquier alimento&nbsp;que te parezca, nosotros te dejamos esta que nos encanta. No olvides ali&ntilde;arla y salpimentarla, incluso est&aacute; deliciosa con alguna especia como el piment&oacute;n o el comino.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    15\/20\n                                \n\n                                                                    Mini pizzas de calabaci\u0301n\n                                \n                                                                    Para esta pizza necesitas, calabac&iacute;n, tomate frito, queso mozarella y peperoni o cualquier guarnici&oacute;n que quieras a&ntilde;adirle a tus pizzas. Lo primero es cortar el calabac&iacute;n en rodajas y hornearlas hasta que est&eacute;n casi hechas del todo. Seguidamente, poner&nbsp;una base de tomate encima de cada rodaja, el queso y la guarnici&oacute;n escogida. De vuelta al horno unos minutos hasta que se acabe de dorar y...&iexcl;listo para disfrutar! Una receta sencilla, r&aacute;pida y deliciosa hasta para los m&aacute;s peque&ntilde;os de la casa.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                                                                                                                                                \n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    16\/20\n                                \n\n                                                                    Lasan\u0303a fri\u0301a\n                                \n                                                                    Tomate, mozarella y albahaca. Nada m&aacute;s ni nada menos. Lo puedes ali&ntilde;ar con vinagre de m&oacute;dena para darle ese toque dulce. Tambi&eacute;n puedes a&ntilde;adirle at&uacute;n en lata para que sea una receta m&aacute;s completa.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    17\/20\n                                \n\n                                                                    Quesadillas de pollo con mozzarella\n                                \n                                                                    Corta el pollo en daditos o tiras y coc&iacute;nalo a la plancha con un poco de aceite de oliva virgen extra. En otra sart&eacute;n, pon a calentar la tortilla, hasta que quede un poquito dorada.&nbsp;Cuando este lista, a&ntilde;&aacute;dele mozzarella, ya que es uno de los quesos m&aacute;s bajos en grasas. A continuaci&oacute;n, a&ntilde;ade tambi&eacute;n el pollo y dobla&nbsp;la tortilla por la mitad, para que adopte la forma de una media luna. Dale la vuelta para que se dore por la otra cara y, posteriormente, ret&iacute;rala del fuego y c&oacute;rtala en tri&aacute;ngulos.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    18\/20\n                                \n\n                                                                    Rollitos de berenjena con espinacas y queso feta\n                                \n                                                                    Precalentamos el horno a 180&ordm; y cortamos la berenjena en l&aacute;minas muy finas, de 1 cm aproximadamente. Les a&ntilde;adimos un poco de sal y las dejamos reposar, mientras el horno se calienta. A continuaci&oacute;n, preparamos una bandeja de horno con un poco de aceite de oliva virgen extra, para poner encima las l&aacute;minas de berenjena. Mientras tanto, cocemos las espinacas y cortamos el queso feta a daditos.&nbsp;\r\n\r\nTranscurridos 10 minutos, sacamos las l&aacute;minas del horno y, en cuanto est&eacute;n lista las espinacas, las a&ntilde;adimos encima de las lonchas y hacemos lo mismo con el queso. Por &uacute;ltimo, enrollamos las l&aacute;minas y, incluso, podemos ayudarnos de un palillo para una mejor sujeci&oacute;n.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                                                                                                                                                \n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    19\/20\n                                \n\n                                                                    Wrap de Kale\n                                \n                                                                    El wrap de Kale es una receta rica en nutrientes, vitaminas y propiedades antioxidantes. Para elaborarlo, corta una cebolla y un tomate en trocitos muy peque&ntilde;os. Coc&iacute;nalos&nbsp;en una sart&eacute;n con aceite de oliva virgen extra,&nbsp;y a&ntilde;ade las especies que desees: comino, cilantro o c&uacute;rcuma. Por otro lado, cocina la col rizada o kale,&nbsp;salpimi&eacute;ntala y, acto seguido, a&ntilde;ade un chorrito de zumo de lim&oacute;n. De este modo, conseguir&aacute;s darle un toque especial y delicioso al wrap.\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                                                                    \n                    \n                        \n                            \n                            \n                                \n                                \n                                    20\/20\n                                \n\n                                                                    Bu\u00f1uelos de calabac\u00edn al horno\n                                \n                                                                    Pelar y rallar el calabac&iacute;n, a&ntilde;adirle sal y colocarlo en un colador, presionando para eliminar el agua que contiene. Poner en un recipiente el calabac&iacute;n, queso fresco, harina de fuerza, levadura fresca, 2 diente de ajo, cebolla,&nbsp;or&eacute;gano y pan rallado.&nbsp;\r\n\r\nUna vez este lista la masa y con el horno a 180&ordm;,&nbsp;cogemos una bandeja,&nbsp;le a&ntilde;adimos un poco de aceite de oliva y las bolitas que habremos hecho de la mezcla. &iexcl;15 minutitos y listo!\n                                                                \n                                    \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                        \n                                            \n                                                \n                                                    \n                                                        \n                                                        \n                                                    \n                                                \n                                            \n                                        \n                                    \n                                \n                            \n                        \n                    \n\n                    \n                                    \n        \n            jQuery(function ($) {\n                var currentData,\n                    originalData,\n                    currentItem,\n                    timeout,\n                    firstItem = $('[data-role=\"gallery-asset\"]:first'),\n                    lastItem = $('[data-role=\"gallery-asset\"]:last'),\n                    totalItems = $('[data-role=\"gallery-asset\"]').length,\n                    loading = false;\n\n                $(\"img.lazy\").lazyload();\n\n                originalData = {\n                    'title': $('title').text(),\n                    'description': $('meta[property=\"og:description\"]').attr('content'),\n                    'url': $('meta[property=\"og:url\"]').attr('content'),\n                    'image': {\n                        'url': $('meta[property=\"og:image\"]').attr('content'),\n                        'width': $('meta[property=\"og:image:width\"]').attr('content'),\n                        'height': $('meta[property=\"og:image:height\"]').attr('content'),\n                    }\n                };\n                currentData = JSON.stringify(originalData);\n\n                $(window).scroll(function () {\n                        if (timeout) {\n                            clearTimeout(timeout);\n                            timeout = null;\n                        }\n                        timeout = setTimeout(loadData, 200);\n                });\n\n                if ($('[data-role=\"gallery-asset\"][data-selected]').length > 0) {\n                    setTimeout(function () {\n                        $('html,body').animate(\n                            {\n                                scrollTop: $('[data-role=\"gallery-asset\"][data-selected]').offset().top\n                            },\n                            400\n                        );\n                    }, 500)\n                }\n\n                function changeMetadata (scrollTop, data)\n                {\n                    var found = false,\n                        head = null,\n                        itemTop = 0,\n                        itemHeight = 0,\n                        element = null,\n                        banner,\n                        count;\n\n                    if (\n                        firstItem.length > 0\n                        && scrollTop >= firstItem.offset().top\n                        && scrollTop = itemTop) {\n                                banner = currentItem.next('[data-role=\"banner\"]');\n                                if (banner.length > 0) {\n                                    itemTop += banner.outerHeight(true);\n                                }\n                                if (scrollTop  0) {\n                                        data.title = element.text();\n                                    }\n                                    element = $('[data-role=\"description\"]', currentItem);\n                                    if (element.length > 0) {\n                                        data.description = element.text();\n                                    }\n                                    element = $('[data-role=\"image\"]', currentItem);\n                                    if (element.length > 0) {\n                                        data.image = {\n                                            'url': element.attr('src'),\n                                            'width': element.data('width'),\n                                            'height': element.data('height'),\n                                        };\n                                    }\n                                    data.url = currentItem.data('link');\n                                    found = true;\n                                } else {\n                                    if (banner.length > 0) {\n                                        currentItem = banner.next();\n                                    } else {\n                                        currentItem = currentItem.next();\n                                    }\n                                }\n                            } else {\n                                if (banner.length > 0) {\n                                    currentItem = banner.prev();\n                                } else {\n                                    currentItem = currentItem.prev();\n                                }\n                            }\n                            count++;\n                        }\n                    }\n\n                    if (currentData != JSON.stringify(data)) {\n                        head = $('head');\n                        $('title', head).text(data.title);\n                        $('meta[property=\"og:title\"]', head).attr('content', data.title);\n                        $('meta[name=\"title\"]', head).attr('content', data.title);\n                        $('meta[name=\"description\"]', head).attr('content', data.description);\n                        $('meta[property=\"og:description\"]', head).attr('content', data.description);\n                        $('meta[name=\"twitter:description\"]', head).attr('content', data.description);\n                        $('meta[name=\"twitter:image:src\"]', head).attr('content', data.image.url);\n                        $('meta[property=\"og:image\"]', head).attr('content', data.image.url);\n                        $('meta[property=\"og:image:width\"]', head).attr('content', data.image.width);\n                        $('meta[property=\"og:image:height\"]', head).attr('content', data.image.height);\n                        $('meta[name=\"twitter:url\"]', head).attr('content', data.url);\n                        $('meta[property=\"og:url\"]', head).attr('content', data.url);\n                        try {\n                            if (typeof(history.replaceState) !== \"undefined\") {\n                                history.replaceState({}, data.title, data.url);\n                            }\n                            if(typeof(ga) !== 'undefined') {\n                                ga('send', { hitType: 'pageview', page: data.url });\n                            }\n                            if(typeof(COMSCORE) !== 'undefined') {\n                                COMSCORE.beacon({c1: \"2\", c2: \"22656911\"});\n                                if (typeof(comscorePageViewUrl) !== 'undefined') {\n                                    $.get(comscorePageViewUrl + '&t=' +  Date.now());\n                                }\n                            }\n                            if (typeof(dataLayer) !== \"undefined\") {\n                                var internReferer = (\n                                    (document.referrer.indexOf(document.domain) != -1)\n                                    || !document.referrer\n                                );\n\n                                dataLayer.setPage(\n                                    data.url,\n                                    'gallery',\n                                    false,\n                                    '',\n                                    (internReferer ? 'intern' : 'extern'),\n                                    '',\n                                    ''\n                                );\n                            }\n                        } catch (error) {}\n                        currentData = JSON.stringify(data);\n                    }\n                }\n\n                function loadBanners (scrollTop, windowHeight)\n                {\n                    var first = false;\n\n                    $('.gallery-banner.banner-loading').each(function () {\n                        var offset = $(this).offset();\n                        if (scrollTop "}</script>



    <div class="csl-inner csl-hot">
        <article>
            <div class="article-header">
                                    <a href="https://www.objetivobienestar.com/alimentacion-saludable" title="Alimentación">
                        <em>Alimentación</em>
                    </a>
                                <time datetime="06/05/2019" title="6 de mayo de 2019">6 de mayo de 2019</time>
                <h1>20 comidas sanas que se preparan en 15 minutos</h1>
                                    <h2>Tener poco tiempo para cocinar no está reñido con comer sano. Elegir productos de temporada y planificar tus menús son recursos para cuidar tu alimentación.</h2>
                            </div>
            <span class="author-info">
                    <div class="sponsor">
                                                                                                                        </div>
                                                            <a href="https://www.objetivobienestar.com/redaccion-objetivo-bienestar_3_115.html" title="Objetivo Bienestar">
                            <span class="img">
                                
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/28/38/09/logo-objetivo-bienestar-autor-ok.jpg" title="Objetivo Bienestar" alt="Objetivo Bienestar" height="" width="" data-prosrcset="" data-original="https://www.objetivobienestar.com/uploads/s1/28/38/09/logo-objetivo-bienestar-autor-ok.jpg" class="cs-responsive-image">
                            </span>
                        </a>
                                        <p>por<br>
                                                    <a href="https://www.objetivobienestar.com/redaccion-objetivo-bienestar_3_115.html" title="Objetivo Bienestar">
                                                    <em>Objetivo Bienestar</em>
                                                    </a>
                                            </p>
                                <div class="addthis_sharing_toolbox" data-url="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102.html" data-title="20 comidas sanas que se preparan en 15 minutos"></div>
            </span>
                            <figure class="article-asset">
                    
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/32/57/23/iStock_93400103_MEDIUM_1_780x462.jpg" title="comidas sanas 15 minutos" alt="comidas sanas 15 minutos" height="" width="" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/57/23/iStock_93400103_MEDIUM_1_780x462.jpg" data-original="https://www.objetivobienestar.com/uploads/s1/32/57/22/iStock_93400103_MEDIUM.jpg" class="cs-responsive-image">
                                        </figure>
                        <main>
                <div class="article-body">
                    <p>Con la llegada de la primavera, apetecen comidas ligeras y frescas. Para ello, existen una infinidad de recetas saludables y variadas que puedes preparar rápidamente para mentener una dieta equilibrada y deliciosa.</p>

<p>Disfrutar comiendo debería ser una obligación, por eso, queremos que intentes <strong>mejorar la manera en la que nutres tu cuerpo </strong>para que tenga toda la energía necesaria y para que no te aburras ni comiendo ni cocinando. Cuantos más alimentos y productos te gusten, más variedad de platos podrás cocinar, pero aún que seas una de esas personas a las que no les gusta a penas nada, puedes encontrar la manera de adaptar los platos y recetas según tus especiales gustos.</p><div class="banner">        <div id="smartIntxt"></div></div>

<p>Te proponemos <strong>20 recetas sencillas de comidas sanas y fáciles,</strong> para comer o cenar, que podrás preparar aunque en tu rutina reine la queja “a mi día le faltan horas”. Desde<strong><a data-external="0" href="https://www.objetivobienestar.com/prepara-tu-propia-pasta-casera_892_102.html" rel="follow" target="_self" title="Prepara tu propia pasta casera"> pasta</a></strong> con diferentes salsas o guarniciones, pasando por <strong>pescado o pollo y hasta deliciosas<a data-external="0" href="https://www.objetivobienestar.com/receta-ensalada-oriental-delicias-kitchen_11601_102.html" rel="follow" target="_self" title="Ensalada oriental de pepino y wakame"> ensaladas</a></strong> que nada tienen que ver con las típicas tan aburridas de lechuga y tomate.</p>

<p>Es importante, para preparar platos saludables, que uses los <strong>productos de temporada</strong> según la época del año. Eso, no solo hará que las recetas sean mucho más económicas, sinó que también estarán mucho más sabrosas. Lo mejor de estas <strong>20 ideas </strong>que te proponemos es que, también te las puedes llevar en<strong> <a data-external="0" href="https://www.objetivobienestar.com/menu-semanal-taper_11881_102.html" rel="follow" target="_self" title="Menú para comer sano y de táper toda la semana">táper</a> a la oficina o al trabajo</strong>, incluso puedes hacer más cantidad y repetir a lo largo de la semana.</p>

<p>¿Te apetece probar alguna?</p>

<p><div class="galleries">
                                                                                
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325332.html" data-id="325332"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/53/32/iStock_83805537_MEDIUM.jpg" data-role="image" title="Ensalada de brócoli, zanahoria y nueces" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/53/33/iStock_83805537_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Ensalada de brócoli, zanahoria y nueces" data-width="1697" data-height="1131"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>1</span>/20
                                </div>

                                                                    <h3 data-role="title">Ensalada de brócoli, zanahoria y nueces</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Corta el br&oacute;coli en ramilletes y cu&eacute;celo en una cazuela con agua y sal durante 5 minutos. Esc&uacute;rrelo y res&eacute;rvalo. Pela las zanahoria, r&aacute;yalas y a&ntilde;&aacute;delas al br&oacute;coli. Prepara, en un vaso, una vinagreta con aceite y zumo de lim&oacute;n para aderezar la ensalada. Por &uacute;ltimo, pica un pu&ntilde;ado de nueces e incorp&oacute;ralas al plato.&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325332.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Ensalada%20de%20br%C3%B3coli%2C%20zanahoria%20y%20nueces&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325332.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325332.html&media=https://www.objetivobienestar.com/uploads/s1/32/53/32/iStock_83805537_MEDIUM.jpg&description=Ensalada%20de%20br%C3%B3coli%2C%20zanahoria%20y%20nueces">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Ensalada%20de%20br%C3%B3coli%2C%20zanahoria%20y%20nueces%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325332.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325317.html" data-id="325317"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/53/17/iStock_29317614_MEDIUM.jpg" data-role="image" title="Espaguetis con revuelto de setas y gambas" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/53/18/iStock_29317614_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Espaguetis con revuelto de setas y gambas" data-width="1697" data-height="1131"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>2</span>/20
                                </div>

                                                                    <h3 data-role="title">Espaguetis con revuelto de setas y gambas</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Hierve los espaguetis en una cazuela. Por otro lado, pon a calentar una sart&eacute;n con aceite. Dora un ajo laminado. Agrega las setas (que deber&aacute;s lavar y escurrir antes) y salt&eacute;alas durante 10 minutos. A&ntilde;ade las gambas peladas y salt&eacute;alas. Incorpora los huevos batidos. Para que el aspecto sea el de un revoltillo y no el de una tortilla a la francesa, tienes que ir retirando la sart&eacute;n del fuego e ir removiendo la mezcla para cuajar bien el huevo.&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325317.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Espaguetis%20con%20revuelto%20de%20setas%20y%20gambas&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325317.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325317.html&media=https://www.objetivobienestar.com/uploads/s1/32/53/17/iStock_29317614_MEDIUM.jpg&description=Espaguetis%20con%20revuelto%20de%20setas%20y%20gambas">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Espaguetis%20con%20revuelto%20de%20setas%20y%20gambas%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325317.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325303.html" data-id="325303"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/53/03/iStock_77981093_MEDIUM.jpg" data-role="image" title="Ensalada de lentejas con calabaza, hummus y almendra" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/53/04/iStock_77981093_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Ensalada de lentejas con calabaza, hummus y almendra" data-width="1385" data-height="1385"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>3</span>/20
                                </div>

                                                                    <h3 data-role="title">Ensalada de lentejas con calabaza, hummus y almendra</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Escurre un bote de lentejas, p&aacute;sales un agua y res&eacute;rvalas en un bol. Corta y cuece la calabaza y m&eacute;zclala con las lentejas. Pica un pu&ntilde;ado de almendras y a&ntilde;&aacute;delas. Al&iacute;&ntilde;ala con sal y aceite de oliva virgen. Aparte, prepara el <a href="https://www.objetivobienestar.com/3-recetas-de-salsas-saludables-hummus-guacamole-y-baba-ganoush_4821_102.html">hummus</a>. Una vez tenga la textura deseada, a&ntilde;ade unas cucharadas por encima a la ensalada.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325303.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Ensalada%20de%20lentejas%20con%20calabaza%2C%20hummus%20y%20almendra&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325303.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325303.html&media=https://www.objetivobienestar.com/uploads/s1/32/53/03/iStock_77981093_MEDIUM.jpg&description=Ensalada%20de%20lentejas%20con%20calabaza%2C%20hummus%20y%20almendra">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Ensalada%20de%20lentejas%20con%20calabaza%2C%20hummus%20y%20almendra%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325303.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                                                                                                                                                <div class="gallery-banner banner-loading" data-role="banner" data-format="MPU3"></div>
                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325288.html" data-id="325288"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/52/88/iStock_36335356_MEDIUM.jpg" data-role="image" title="Caldo de verduras rápido" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/52/89/iStock_36335356_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Caldo de verduras rápido" data-width="1702" data-height="1127"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>4</span>/20
                                </div>

                                                                    <h3 data-role="title">Caldo de verduras rápido</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Limpia y pela verduras variadas como el apio, la zanahoria, el puerro o el nabo y c&oacute;rtalas a trocitos. Rehoga en una cazuela con un chorrito de aceite la cebolla y el puerro hasta que se doren. A&ntilde;ade el resto de verduras y salt&eacute;alas durante 5 minutos. Incorpora agua y hierbas arom&aacute;ticas como el tomillo y el laurel. Cu&eacute;celo todo a fuego suave durante 15 minutos. Cuendo est&eacute; listo, cu&eacute;lalo.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325288.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Caldo%20de%20verduras%20r%C3%A1pido&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325288.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325288.html&media=https://www.objetivobienestar.com/uploads/s1/32/52/88/iStock_36335356_MEDIUM.jpg&description=Caldo%20de%20verduras%20r%C3%A1pido">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Caldo%20de%20verduras%20r%C3%A1pido%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325288.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325273.html" data-id="325273"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/52/73/iStock_89669089_MEDIUM.jpg" data-role="image" title="Cuscús con pollo, verduras y cúrcuma" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/52/74/iStock_89669089_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Cuscús con pollo, verduras y cúrcuma" data-width="1695" data-height="1132"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>5</span>/20
                                </div>

                                                                    <h3 data-role="title">Cuscús con pollo, verduras y cúrcuma</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Saltea una cebolla bien picada en la sart&eacute;n hasta que est&eacute; dorada. A&ntilde;ade pimiento verde, calabac&iacute;n y una pechuga de pollo troceada. Reh&oacute;galo todo durante 15 minutos. Por otro lado, lleva a ebullici&oacute;n 250 ml de agua con un chorrito de aceite y sal. Cuando el agua hierva, retira el recipiente del fuego y vierte 250 g de cusc&uacute;s. Remu&eacute;velo y d&eacute;jalo reposar 3 minutos. A&ntilde;ade una cucharada peque&ntilde;a de mantequilla y coloca de nuevo el recipiente en el fuego a baja temperatura durante 2-3 minutos, remueve el cusc&uacute;s con un tenedor. Incorpora el pollo y las verduras salteadas al cusc&uacute;s y sazona el plato con una cucharadita de c&uacute;rcuma.&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325273.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Cusc%C3%BAs%20con%20pollo%2C%20verduras%20y%20c%C3%BArcuma&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325273.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325273.html&media=https://www.objetivobienestar.com/uploads/s1/32/52/73/iStock_89669089_MEDIUM.jpg&description=Cusc%C3%BAs%20con%20pollo%2C%20verduras%20y%20c%C3%BArcuma">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Cusc%C3%BAs%20con%20pollo%2C%20verduras%20y%20c%C3%BArcuma%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325273.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325258.html" data-id="325258"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/52/58/iStock_90460361_MEDIUM.jpg" data-role="image" title="Espaguetis con espinacas, taquitos de jamón y ajos tiernos" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/52/59/iStock_90460361_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Espaguetis con espinacas, taquitos de jamón y ajos tiernos" data-width="1697" data-height="1131"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>6</span>/20
                                </div>

                                                                    <h3 data-role="title">Espaguetis con espinacas, taquitos de jamón y ajos tiernos</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Cuece por un lado las espinacas y por otro la pasta. Saltea, en una sart&eacute;n con aceite, los ajos tiernos previamente lavados y cortados a trozos peque&ntilde;os. Para terminar, a&ntilde;ade unos tacos de jam&oacute;n serrano y reh&oacute;galos en la sart&eacute;n. Incorpora las espinacas y los espaguetis para mezclar todos los ingredientes.</p>

<p>&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325258.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Espaguetis%20con%20espinacas%2C%20taquitos%20de%20jam%C3%B3n%20y%20ajos%20tiernos&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325258.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325258.html&media=https://www.objetivobienestar.com/uploads/s1/32/52/58/iStock_90460361_MEDIUM.jpg&description=Espaguetis%20con%20espinacas%2C%20taquitos%20de%20jam%C3%B3n%20y%20ajos%20tiernos">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Espaguetis%20con%20espinacas%2C%20taquitos%20de%20jam%C3%B3n%20y%20ajos%20tiernos%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325258.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                                                                                                                                                <div class="gallery-banner banner-loading" data-role="banner" data-format="MPU4"></div>
                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325243.html" data-id="325243"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/52/43/iStock_67696937_MEDIUM.jpg" data-role="image" title="Lentejas con salmón, eneldo y comino" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/52/44/iStock_67696937_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Lentejas con salmón, eneldo y comino" data-width="1697" data-height="1131"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>7</span>/20
                                </div>

                                                                    <h3 data-role="title">Lentejas con salmón, eneldo y comino</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Enjuaga las lentejas y res&eacute;rvalas. Pela y corta una cebolla a trozos peque&ntilde;os. Calienta una cazuela con aceite y dora las verduras y un ajo. Salpim&eacute;ntalo hasta que este pochado. A&ntilde;ade a las verduras comino y eneldo y c&uacute;brelas de caldo de pescado o de agua y cu&eacute;celo todo durante 4 minutos. Despu&eacute;s, cocina el salm&oacute;n 3 minutos por la parte de abajo y unos segundos por encima. Cuando est&eacute; listo, montamos una base con las lentejas y las verduras y colocamos encima el salm&oacute;n.&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325243.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Lentejas%20con%20salm%C3%B3n%2C%20eneldo%20y%20comino&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325243.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325243.html&media=https://www.objetivobienestar.com/uploads/s1/32/52/43/iStock_67696937_MEDIUM.jpg&description=Lentejas%20con%20salm%C3%B3n%2C%20eneldo%20y%20comino">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Lentejas%20con%20salm%C3%B3n%2C%20eneldo%20y%20comino%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325243.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325229.html" data-id="325229"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/52/29/iStock_94580877_MEDIUM.jpg" data-role="image" title="Ensalada de calabaza con aguacate, tomate y pepino" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/52/30/iStock_94580877_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Ensalada de calabaza con aguacate, tomate y pepino" data-width="1599" data-height="1200"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>8</span>/20
                                </div>

                                                                    <h3 data-role="title">Ensalada de calabaza con aguacate, tomate y pepino</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Lava y pela las verduras. Raya muy fina la calabaza y trocea el aguacate, el tomate y el pepino en dados peque&ntilde;os. Para el aderezo final, usa aceite de oliva virgen extra, zumo de lim&oacute;n, salsa de soja y s&eacute;samo crudo.&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325229.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Ensalada%20de%20calabaza%20con%20aguacate%2C%20tomate%20y%20pepino&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325229.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325229.html&media=https://www.objetivobienestar.com/uploads/s1/32/52/29/iStock_94580877_MEDIUM.jpg&description=Ensalada%20de%20calabaza%20con%20aguacate%2C%20tomate%20y%20pepino">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Ensalada%20de%20calabaza%20con%20aguacate%2C%20tomate%20y%20pepino%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325229.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325214.html" data-id="325214"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/52/14/iStock_23547152_MEDIUM.jpg" data-role="image" title="Escarola con pera y pasas" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/52/15/iStock_23547152_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Escarola con pera y pasas" data-width="1697" data-height="1131"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>9</span>/20
                                </div>

                                                                    <h3 data-role="title">Escarola con pera y pasas</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Lava la escarola, troc&eacute;ala y col&oacute;cala en una fuente. Agrega la pera cortada en dados, las pasas y pipas de girasol. Prepara un aderezo con sal, aceite de oliva y vinagre blanco de manzana.</p>

<p>&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325214.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Escarola%20con%20pera%20y%20pasas&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325214.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325214.html&media=https://www.objetivobienestar.com/uploads/s1/32/52/14/iStock_23547152_MEDIUM.jpg&description=Escarola%20con%20pera%20y%20pasas">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Escarola%20con%20pera%20y%20pasas%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325214.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                                                                                                                                                <div class="gallery-banner banner-loading" data-role="banner" data-format="MPU3"></div>
                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/325199.html" data-id="325199"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/32/51/99/iStock_14230260_MEDIUM.jpg" data-role="image" title="Judías verdes con picada de ajo" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/32/52/00/iStock_14230260_MEDIUM_1_780x462.jpg" class="cs-responsive-image lazy" alt="Judías verdes con picada de ajo" data-width="1697" data-height="1131"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>10</span>/20
                                </div>

                                                                    <h3 data-role="title">Judías verdes con picada de ajo</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Tan sencillo como jud&iacute;as verdes y ajo previamente dorado en la sart&eacute;n. El ajo le dar&aacute; un sabor diferente a el t&iacute;pico plato de verdura.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325199.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Jud%C3%ADas%20verdes%20con%20picada%20de%20ajo&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325199.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325199.html&media=https://www.objetivobienestar.com/uploads/s1/32/51/99/iStock_14230260_MEDIUM.jpg&description=Jud%C3%ADas%20verdes%20con%20picada%20de%20ajo">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Jud%C3%ADas%20verdes%20con%20picada%20de%20ajo%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F325199.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/587425.html" data-id="587425"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/58/74/25/aguacates-rellenos-de-atu-n.jpeg" data-role="image" title="Aguacates rellenos de atún" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/58/74/26/aguacates-rellenos-de-atu-n_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Aguacates rellenos de atún" data-width="1070" data-height="713"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>11</span>/20
                                </div>

                                                                    <h3 data-role="title">Aguacates rellenos de atún</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Necesitas aguacate, latas de at&uacute;n en aceite, pimiento escalivado y mayonesa. La elaboraci&oacute;n es muy sencilla ya que, solo hay que&nbsp;cortar por la mitad los aguacates y vaciarlos. Mezclar todos los ingredientes y usar la mezcla para volver a rellenar el aguacate. Lo mejor de esta receta es que puedes incorporar o eliminar cualquier producto seg&uacute;n tus gustos.&nbsp;</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587425.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Aguacates%20rellenos%20de%20atu%CC%81n&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587425.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587425.html&media=https://www.objetivobienestar.com/uploads/s1/58/74/25/aguacates-rellenos-de-atu-n.jpeg&description=Aguacates%20rellenos%20de%20atu%CC%81n">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Aguacates%20rellenos%20de%20atu%CC%81n%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587425.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/587438.html" data-id="587438"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/58/74/38/tortilla-de-espinacas.jpeg" data-role="image" title="Tortilla de espinacas" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/58/74/39/tortilla-de-espinacas_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Tortilla de espinacas" data-width="1070" data-height="713"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>12</span>/20
                                </div>

                                                                    <h3 data-role="title">Tortilla de espinacas</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Todo el mundo sabe como hacer una trotilla. Para esta necesitas huevos y espinacas. Lo primero es batir el huevo, salpimentarlo y mientras tanto, por otro lado, hay que ir&nbsp;haciendo las espinacas con un poco de aceite. El resto ya es conocido: se junta todo y &iexcl;a la sart&eacute;n! hasta que est&eacute; hecha. Puedes a&ntilde;adirle patata, cebolla o cualquier otro vegetal que te guste.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587438.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Tortilla%20de%20espinacas&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587438.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587438.html&media=https://www.objetivobienestar.com/uploads/s1/58/74/38/tortilla-de-espinacas.jpeg&description=Tortilla%20de%20espinacas">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Tortilla%20de%20espinacas%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587438.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                                                                                                                                                <div class="gallery-banner banner-loading" data-role="banner" data-format="MPU4"></div>
                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/587451.html" data-id="587451"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/58/74/51/guisantes-con-jamo-n.jpeg" data-role="image" title="Guisantes con jamón" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/58/74/52/guisantes-con-jamo-n_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Guisantes con jamón" data-width="1070" data-height="736"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>13</span>/20
                                </div>

                                                                    <h3 data-role="title">Guisantes con jamón</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Saltear los guisantes con daditos o tiras finas de jam&oacute;n y &iexcl;listo! Tambi&eacute;n puedes a&ntilde;adirle al salteado cebolla para darle m&aacute;s textura y otro sabor. Tan sencillo y f&aacute;cil de preparar que la har&aacute;s en grandes cantidades para aprovecharla en otras comidas a lo largo de la&nbsp;semana.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587451.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Guisantes%20con%20jamo%CC%81n&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587451.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587451.html&media=https://www.objetivobienestar.com/uploads/s1/58/74/51/guisantes-con-jamo-n.jpeg&description=Guisantes%20con%20jamo%CC%81n">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Guisantes%20con%20jamo%CC%81n%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587451.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/587464.html" data-id="587464"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/58/74/64/ensalada-fri-a-de-garbanzos.jpeg" data-role="image" title="Ensalada fría de garbanzos" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/58/74/65/ensalada-fri-a-de-garbanzos_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Ensalada fría de garbanzos" data-width="1070" data-height="713"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>14</span>/20
                                </div>

                                                                    <h3 data-role="title">Ensalada fría de garbanzos</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Para preparar esta ensalada a base de legumbres necesitas un bote de garbanzos cocidos, pimiento rojo y verde, cebolla, tomatitos cherry, olivas negras y ma&iacute;z. Aunque puedes a&ntilde;adirle cualquier alimento&nbsp;que te parezca, nosotros te dejamos esta que nos encanta. No olvides ali&ntilde;arla y salpimentarla, incluso est&aacute; deliciosa con alguna especia como el piment&oacute;n o el comino.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587464.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Ensalada%20fri%CC%81a%20de%20garbanzos&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587464.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587464.html&media=https://www.objetivobienestar.com/uploads/s1/58/74/64/ensalada-fri-a-de-garbanzos.jpeg&description=Ensalada%20fri%CC%81a%20de%20garbanzos">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Ensalada%20fri%CC%81a%20de%20garbanzos%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587464.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/587477.html" data-id="587477"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/58/74/77/mini-pizzas-de-calabaci-n.jpeg" data-role="image" title="Mini pizzas de calabacín" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/58/74/78/mini-pizzas-de-calabaci-n_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Mini pizzas de calabacín" data-width="1070" data-height="711"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>15</span>/20
                                </div>

                                                                    <h3 data-role="title">Mini pizzas de calabacín</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Para esta pizza necesitas, calabac&iacute;n, tomate frito, queso mozarella y peperoni o cualquier guarnici&oacute;n que quieras a&ntilde;adirle a tus pizzas. Lo primero es cortar el calabac&iacute;n en rodajas y hornearlas hasta que est&eacute;n casi hechas del todo. Seguidamente, poner&nbsp;una base de tomate encima de cada rodaja, el queso y la guarnici&oacute;n escogida. De vuelta al horno unos minutos hasta que se acabe de dorar y...&iexcl;listo para disfrutar! Una receta sencilla, r&aacute;pida y deliciosa hasta para los m&aacute;s peque&ntilde;os de la casa.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587477.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Mini%20pizzas%20de%20calabaci%CC%81n&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587477.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587477.html&media=https://www.objetivobienestar.com/uploads/s1/58/74/77/mini-pizzas-de-calabaci-n.jpeg&description=Mini%20pizzas%20de%20calabaci%CC%81n">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Mini%20pizzas%20de%20calabaci%CC%81n%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587477.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                                                                                                                                                <div class="gallery-banner banner-loading" data-role="banner" data-format="MPU3"></div>
                    
                                                                                    
                    <div class="figure portrait" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/587529.html" data-id="587529"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/58/75/29/lasan-a-fri-a.jpeg" data-role="image" title="Lasaña fría" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/58/75/30/lasan-a-fri-a_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Lasaña fría" data-width="1070" data-height="1349"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>16</span>/20
                                </div>

                                                                    <h3 data-role="title">Lasaña fría</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Tomate, mozarella y albahaca. Nada m&aacute;s ni nada menos. Lo puedes ali&ntilde;ar con vinagre de m&oacute;dena para darle ese toque dulce. Tambi&eacute;n puedes a&ntilde;adirle at&uacute;n en lata para que sea una receta m&aacute;s completa.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587529.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Lasan%CC%83a%20fri%CC%81a&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587529.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587529.html&media=https://www.objetivobienestar.com/uploads/s1/58/75/29/lasan-a-fri-a.jpeg&description=Lasan%CC%83a%20fri%CC%81a">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Lasan%CC%83a%20fri%CC%81a%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F587529.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/631612.html" data-id="631612"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/63/16/12/istock-628233476.jpeg" data-role="image" title="Quesadillas de pollo con mozzarella" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/63/16/13/istock-628233476_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Quesadillas de pollo con mozzarella" data-width="1254" data-height="836"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>17</span>/20
                                </div>

                                                                    <h3 data-role="title">Quesadillas de pollo con mozzarella</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Corta el pollo en daditos o tiras y coc&iacute;nalo a la plancha con un poco de aceite de oliva virgen extra. En otra sart&eacute;n, pon a calentar la tortilla, hasta que quede un poquito dorada.&nbsp;Cuando este lista, a&ntilde;&aacute;dele mozzarella, ya que es uno de los quesos m&aacute;s bajos en grasas. A continuaci&oacute;n, a&ntilde;ade tambi&eacute;n el pollo y dobla&nbsp;la tortilla por la mitad, para que adopte la forma de una media luna. Dale la vuelta para que se dore por la otra cara y, posteriormente, ret&iacute;rala del fuego y c&oacute;rtala en tri&aacute;ngulos.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631612.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Quesadillas%20de%20pollo%20con%20mozzarella&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631612.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631612.html&media=https://www.objetivobienestar.com/uploads/s1/63/16/12/istock-628233476.jpeg&description=Quesadillas%20de%20pollo%20con%20mozzarella">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Quesadillas%20de%20pollo%20con%20mozzarella%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631612.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/631640.html" data-id="631640"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/63/16/40/istock-467367464.jpeg" data-role="image" title="Rollitos de berenjena con espinacas y queso feta" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/63/16/41/istock-467367464_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Rollitos de berenjena con espinacas y queso feta" data-width="1231" data-height="852"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>18</span>/20
                                </div>

                                                                    <h3 data-role="title">Rollitos de berenjena con espinacas y queso feta</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Precalentamos el horno a 180&ordm; y cortamos la berenjena en l&aacute;minas muy finas, de 1 cm aproximadamente. Les a&ntilde;adimos un poco de sal y las dejamos reposar, mientras el horno se calienta. A continuaci&oacute;n, preparamos una bandeja de horno con un poco de aceite de oliva virgen extra, para poner encima las l&aacute;minas de berenjena. Mientras tanto, cocemos las espinacas y cortamos el queso feta a daditos.&nbsp;</p>

<p>Transcurridos 10 minutos, sacamos las l&aacute;minas del horno y, en cuanto est&eacute;n lista las espinacas, las a&ntilde;adimos encima de las lonchas y hacemos lo mismo con el queso. Por &uacute;ltimo, enrollamos las l&aacute;minas y, incluso, podemos ayudarnos de un palillo para una mejor sujeci&oacute;n.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631640.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Rollitos%20de%20berenjena%20con%20espinacas%20y%20queso%20feta&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631640.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631640.html&media=https://www.objetivobienestar.com/uploads/s1/63/16/40/istock-467367464.jpeg&description=Rollitos%20de%20berenjena%20con%20espinacas%20y%20queso%20feta">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Rollitos%20de%20berenjena%20con%20espinacas%20y%20queso%20feta%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631640.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                                                                                                                                                <div class="gallery-banner banner-loading" data-role="banner" data-format="MPU4"></div>
                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/631626.html" data-id="631626"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/63/16/26/istock-1038455826.jpeg" data-role="image" title="Wrap de Kale" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/63/16/27/istock-1038455826_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Wrap de Kale" data-width="1254" data-height="837"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>19</span>/20
                                </div>

                                                                    <h3 data-role="title">Wrap de Kale</h3>
                                
                                                                    <div class="cont" data-role="description"><p>El wrap de Kale es una receta rica en nutrientes, vitaminas y propiedades antioxidantes. Para elaborarlo, corta una cebolla y un tomate en trocitos muy peque&ntilde;os. Coc&iacute;nalos&nbsp;en una sart&eacute;n con aceite de oliva virgen extra,&nbsp;y a&ntilde;ade las especies que desees: comino, cilantro o c&uacute;rcuma. Por otro lado, cocina la col rizada o kale,&nbsp;salpimi&eacute;ntala y, acto seguido, a&ntilde;ade un chorrito de zumo de lim&oacute;n. De este modo, conseguir&aacute;s darle un toque especial y delicioso al wrap.</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631626.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Wrap%20de%20Kale&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631626.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631626.html&media=https://www.objetivobienestar.com/uploads/s1/63/16/26/istock-1038455826.jpeg&description=Wrap%20de%20Kale">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Wrap%20de%20Kale%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631626.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                                                                    
                    <div class="figure landscape" data-role="gallery-asset"
                        data-link="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102/631654.html" data-id="631654"
                        >
                        <figure>
                            <img data-original="https://www.objetivobienestar.com/uploads/s1/63/16/54/istock-1139717146.jpeg" data-role="image" title="Buñuelos de calabacín al horno" data-prosrcset="780|462://www.objetivobienestar.com/uploads/s1/63/16/55/istock-1139717146_1_780x462.jpeg" class="cs-responsive-image lazy" alt="Buñuelos de calabacín al horno" data-width="1254" data-height="836"/>
                            <figcaption>
                                
                                <div class="pagin">
                                    <span>20</span>/20
                                </div>

                                                                    <h3 data-role="title">Buñuelos de calabacín al horno</h3>
                                
                                                                    <div class="cont" data-role="description"><p>Pelar y rallar el calabac&iacute;n, a&ntilde;adirle sal y colocarlo en un colador, presionando para eliminar el agua que contiene. Poner en un recipiente el calabac&iacute;n, queso fresco, harina de fuerza, levadura fresca, 2 diente de ajo, cebolla,&nbsp;or&eacute;gano y pan rallado.&nbsp;</p>

<p>Una vez este lista la masa y con el horno a 180&ordm;,&nbsp;cogemos una bandeja,&nbsp;le a&ntilde;adimos un poco de aceite de oliva y las bolitas que habremos hecho de la mezcla. &iexcl;15 minutitos y listo!</p></div>
                                                                <div class="social-share">
                                    <ul>
                                        <li>
                                            <a class="icon-content fb" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631654.html">
                                                <svg alt="Facebook" class="icon-fb" title="Facebook" viewBox="0 0 96.124 96.123" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M72.089,0.02L59.624,0C45.62,0,36.57,9.285,36.57,23.656v10.907H24.037c-1.083,0-1.96,0.878-1.96,1.961v15.803 c0,1.083,0.878,1.96,1.96,1.96h12.533v39.876c0,1.083,0.877,1.96,1.96,1.96h16.352c1.083,0,1.96-0.878,1.96-1.96V54.287h14.654 c1.083,0,1.96-0.877,1.96-1.96l0.006-15.803c0-0.52-0.207-1.018-0.574-1.386c-0.367-0.368-0.867-0.575-1.387-0.575H56.842v-9.246 c0-4.444,1.059-6.7,6.848-6.7l8.397-0.003c1.082,0,1.959-0.878,1.959-1.96V1.98C74.046,0.899,73.17,0.022,72.089,0.02z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content tw" target="_blank" href="https://twitter.com/intent/tweet?text=Bu%C3%B1uelos%20de%20calabac%C3%ADn%20al%20horno&url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631654.html">
                                                <svg alt="Twitter" class="icon-tw" title="Twitter" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M27.996 10.116c-.81.36-1.68.602-2.592.71a4.526 4.526 0 0 0 1.984-2.496 9.037 9.037 0 0 1-2.866 1.095 4.513 4.513 0 0 0-7.69 4.116 12.81 12.81 0 0 1-9.3-4.715 4.49 4.49 0 0 0-.612 2.27 4.51 4.51 0 0 0 2.008 3.755 4.495 4.495 0 0 1-2.044-.564v.057a4.515 4.515 0 0 0 3.62 4.425 4.52 4.52 0 0 1-2.04.077 4.517 4.517 0 0 0 4.217 3.134 9.055 9.055 0 0 1-5.604 1.93A9.18 9.18 0 0 1 6 23.85a12.773 12.773 0 0 0 6.918 2.027c8.3 0 12.84-6.876 12.84-12.84 0-.195-.005-.39-.014-.583a9.172 9.172 0 0 0 2.252-2.336" fill-rule="evenodd"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content pnt" target="_blank" href="http://pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631654.html&media=https://www.objetivobienestar.com/uploads/s1/63/16/54/istock-1139717146.jpeg&description=Bu%C3%B1uelos%20de%20calabac%C3%ADn%20al%20horno">
                                                <svg alt="Pinterest" class="icon-pnt" title="Pinterest" viewBox="0 0 486.392 486.392" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M430.149,135.248C416.865,39.125,321.076-9.818,218.873,1.642 C138.071,10.701,57.512,76.03,54.168,169.447c-2.037,57.029,14.136,99.801,68.399,111.84 c23.499-41.586-7.569-50.676-12.433-80.802C90.222,77.367,252.16-6.718,336.975,79.313c58.732,59.583,20.033,242.77-74.57,223.71 c-90.621-18.179,44.383-164.005-27.937-192.611c-58.793-23.286-90.013,71.135-62.137,118.072 c-16.355,80.711-51.557,156.709-37.3,257.909c46.207-33.561,61.802-97.734,74.57-164.704 c23.225,14.136,35.659,28.758,65.268,31.038C384.064,361.207,445.136,243.713,430.149,135.248z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                        <li>
                                            <a class="icon-content whts" target="_blank" href="whatsapp://send?text=Bu%C3%B1uelos%20de%20calabac%C3%ADn%20al%20horno%20https%3A%2F%2Fwww.objetivobienestar.com%2F10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102%2F631654.html">
                                                <svg alt="Whatsapp" class="icon-whts" title="Whatsapp" viewBox="0 0 308 308" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                                    <g>
                                                        <path d="M227.904,176.981c-0.6-0.288-23.054-11.345-27.044-12.781c-1.629-0.585-3.374-1.156-5.23-1.156 c-3.032,0-5.579,1.511-7.563,4.479c-2.243,3.334-9.033,11.271-11.131,13.642c-0.274,0.313-0.648,0.687-0.872,0.687 c-0.201,0-3.676-1.431-4.728-1.888c-24.087-10.463-42.37-35.624-44.877-39.867c-0.358-0.61-0.373-0.887-0.376-0.887 c0.088-0.323,0.898-1.135,1.316-1.554c1.223-1.21,2.548-2.805,3.83-4.348c0.607-0.731,1.215-1.463,1.812-2.153 c1.86-2.164,2.688-3.844,3.648-5.79l0.503-1.011c2.344-4.657,0.342-8.587-0.305-9.856c-0.531-1.062-10.012-23.944-11.02-26.348 c-2.424-5.801-5.627-8.502-10.078-8.502c-0.413,0,0,0-1.732,0.073c-2.109,0.089-13.594,1.601-18.672,4.802 c-5.385,3.395-14.495,14.217-14.495,33.249c0,17.129,10.87,33.302,15.537,39.453c0.116,0.155,0.329,0.47,0.638,0.922 c17.873,26.102,40.154,45.446,62.741,54.469c21.745,8.686,32.042,9.69,37.896,9.69c0.001,0,0.001,0,0.001,0 c2.46,0,4.429-0.193,6.166-0.364l1.102-0.105c7.512-0.666,24.02-9.22,27.775-19.655c2.958-8.219,3.738-17.199,1.77-20.458 C233.168,179.508,230.845,178.393,227.904,176.981z"></path>
                                                        <path d="M156.734,0C73.318,0,5.454,67.354,5.454,150.143c0,26.777,7.166,52.988,20.741,75.928L0.212,302.716 c-0.484,1.429-0.124,3.009,0.933,4.085C1.908,307.58,2.943,308,4,308c0.405,0,0.813-0.061,1.211-0.188l79.92-25.396 c21.87,11.685,46.588,17.853,71.604,17.853C240.143,300.27,308,232.923,308,150.143C308,67.354,240.143,0,156.734,0z M156.734,268.994c-23.539,0-46.338-6.797-65.936-19.657c-0.659-0.433-1.424-0.655-2.194-0.655c-0.407,0-0.815,0.062-1.212,0.188 l-40.035,12.726l12.924-38.129c0.418-1.234,0.209-2.595-0.561-3.647c-14.924-20.392-22.813-44.485-22.813-69.677 c0-65.543,53.754-118.867,119.826-118.867c66.064,0,119.812,53.324,119.812,118.867 C276.546,215.678,222.799,268.994,156.734,268.994z"></path>
                                                    </g>
                                                </svg>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </figcaption>
                        </figure>
                    </div>

                    
                                    </div>
        <script type="text/javascript">
            jQuery(function ($) {
                var currentData,
                    originalData,
                    currentItem,
                    timeout,
                    firstItem = $('[data-role="gallery-asset"]:first'),
                    lastItem = $('[data-role="gallery-asset"]:last'),
                    totalItems = $('[data-role="gallery-asset"]').length,
                    loading = false;

                $("img.lazy").lazyload();

                originalData = {
                    'title': $('title').text(),
                    'description': $('meta[property="og:description"]').attr('content'),
                    'url': $('meta[property="og:url"]').attr('content'),
                    'image': {
                        'url': $('meta[property="og:image"]').attr('content'),
                        'width': $('meta[property="og:image:width"]').attr('content'),
                        'height': $('meta[property="og:image:height"]').attr('content'),
                    }
                };
                currentData = JSON.stringify(originalData);

                $(window).scroll(function () {
                        if (timeout) {
                            clearTimeout(timeout);
                            timeout = null;
                        }
                        timeout = setTimeout(loadData, 200);
                });

                if ($('[data-role="gallery-asset"][data-selected]').length > 0) {
                    setTimeout(function () {
                        $('html,body').animate(
                            {
                                scrollTop: $('[data-role="gallery-asset"][data-selected]').offset().top
                            },
                            400
                        );
                    }, 500)
                }

                function changeMetadata (scrollTop, data)
                {
                    var found = false,
                        head = null,
                        itemTop = 0,
                        itemHeight = 0,
                        element = null,
                        banner,
                        count;

                    if (
                        firstItem.length > 0
                        && scrollTop >= firstItem.offset().top
                        && scrollTop <= (lastItem.offset().top+lastItem.outerHeight(true))
                    ) {
                        if (!currentItem || currentItem.length == 0) {
                            if (
                                (scrollTop-firstItem.offset().top) <= (
                                    lastItem.offset().top+lastItem.outerHeight(true)-scrollTop
                                )
                            ) {
                                currentItem = firstItem;
                            } else {
                                currentItem = lastItem;
                            }
                        }

                        count = 0;
                        while (!found && currentItem.length > 0 && count <= totalItems) {
                            itemTop = currentItem.offset().top;
                            itemHeight = currentItem.outerHeight(true);
                            banner = currentItem.prev('[data-role="banner"]');
                            if (banner.length > 0) {
                                itemTop -= banner.outerHeight(true);
                                itemHeight += banner.outerHeight(true);
                            }

                            if (scrollTop >= itemTop) {
                                banner = currentItem.next('[data-role="banner"]');
                                if (banner.length > 0) {
                                    itemTop += banner.outerHeight(true);
                                }
                                if (scrollTop <= Math.floor(itemTop + itemHeight)) {
                                    element = $('[data-role="title"]', currentItem);
                                    if (element.length > 0) {
                                        data.title = element.text();
                                    }
                                    element = $('[data-role="description"]', currentItem);
                                    if (element.length > 0) {
                                        data.description = element.text();
                                    }
                                    element = $('[data-role="image"]', currentItem);
                                    if (element.length > 0) {
                                        data.image = {
                                            'url': element.attr('src'),
                                            'width': element.data('width'),
                                            'height': element.data('height'),
                                        };
                                    }
                                    data.url = currentItem.data('link');
                                    found = true;
                                } else {
                                    if (banner.length > 0) {
                                        currentItem = banner.next();
                                    } else {
                                        currentItem = currentItem.next();
                                    }
                                }
                            } else {
                                if (banner.length > 0) {
                                    currentItem = banner.prev();
                                } else {
                                    currentItem = currentItem.prev();
                                }
                            }
                            count++;
                        }
                    }

                    if (currentData != JSON.stringify(data)) {
                        head = $('head');
                        $('title', head).text(data.title);
                        $('meta[property="og:title"]', head).attr('content', data.title);
                        $('meta[name="title"]', head).attr('content', data.title);
                        $('meta[name="description"]', head).attr('content', data.description);
                        $('meta[property="og:description"]', head).attr('content', data.description);
                        $('meta[name="twitter:description"]', head).attr('content', data.description);
                        $('meta[name="twitter:image:src"]', head).attr('content', data.image.url);
                        $('meta[property="og:image"]', head).attr('content', data.image.url);
                        $('meta[property="og:image:width"]', head).attr('content', data.image.width);
                        $('meta[property="og:image:height"]', head).attr('content', data.image.height);
                        $('meta[name="twitter:url"]', head).attr('content', data.url);
                        $('meta[property="og:url"]', head).attr('content', data.url);
                        try {
                            if (typeof(history.replaceState) !== "undefined") {
                                history.replaceState({}, data.title, data.url);
                            }
                            if(typeof(ga) !== 'undefined') {
                                ga('send', { hitType: 'pageview', page: data.url });
                            }
                            if(typeof(COMSCORE) !== 'undefined') {
                                COMSCORE.beacon({c1: "2", c2: "22656911"});
                                if (typeof(comscorePageViewUrl) !== 'undefined') {
                                    $.get(comscorePageViewUrl + '&t=' +  Date.now());
                                }
                            }
                            if (typeof(dataLayer) !== "undefined") {
                                var internReferer = (
                                    (document.referrer.indexOf(document.domain) != -1)
                                    || !document.referrer
                                );

                                dataLayer.setPage(
                                    data.url,
                                    'gallery',
                                    false,
                                    '',
                                    (internReferer ? 'intern' : 'extern'),
                                    '',
                                    ''
                                );
                            }
                        } catch (error) {}
                        currentData = JSON.stringify(data);
                    }
                }

                function loadBanners (scrollTop, windowHeight)
                {
                    var first = false;

                    $('.gallery-banner.banner-loading').each(function () {
                        var offset = $(this).offset();
                        if (scrollTop <= offset.top && ($(this).height() + offset.top) < (scrollTop + windowHeight) && first === false) {
                            var banner = $(this),
                                format = banner.data('format'),
                                content = $('<div id="wfg_ad-' + format + '"></div>').append($('<script type="text/javascript">').append('$pub.display("' + format + '")'));
                            banner.append(content);
                            banner.removeClass('banner-loading');
                            first = true;
                        } else {
                            first = false;
                        }
                    });
                }

                function loadData()
                {
                    var scrollTop, windowHeight;

                    if (!loading) {
                        loading = true;
                        scrollTop = $(window).scrollTop();
                        windowHeight = $(window).height();

                        changeMetadata(scrollTop+windowHeight, JSON.parse(JSON.stringify(originalData)));
                        loadBanners(scrollTop, windowHeight);
                        loading = false;
                    }
                }
            });
        </script></p>
                </div>
            </main>
                                        <ul class="tags">
                                            <li><a href="https://www.objetivobienestar.com/comer-sano_39_119.html" title="Comer sano">Comer sano</a></li>
                                    </ul>
                    </article>
    </div>
    <script type="text/javascript">
        var comscorePageViewUrl = "/_call?controller=ComitiumSuite%5CBundle%5CCSBundle%5CWidgets%5CArticleViewerBody%5CController%5CWidgetController&action=generateComscorePageViewCandidateXMLAction";
    </script>

            <div id="ultimedia_wrapper"></div>
        <script type="text/javascript">
            var ULTIMEDIA_mdtk = "03682638";
            var ULTIMEDIA_zone = "2";
            var ULTIMEDIA_target = "ultimedia_wrapper";
            var ULTIMEDIA_async = false;
        </script>
        <script type="text/javascript" src="//www.ultimedia.com/js/common/smart.js"></script>
    

    <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6 article-bottom">
        <div class="tsubgroup">
            <span>Te recomendamos</span>
        </div>
        <div class="row">
                            <div class="col-xs-6 col-sm-3 col-md-2 col-lg-2">
                    <div class="item">
                                                    <span class="img">
                                <a href="https://www.objetivobienestar.com/veganismo-la-cultura-hegemonica-del-futuro_42253_102.html" title="Veganismo, la cultura hegemónica del futuro">
                                   
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/76/94/veganismo-la-cultura-hegemonica-del-futuro_3_360x213.jpeg" title="Veganismo, la cultura hegemónica del futuro" alt="Veganismo, la cultura hegemónica del futuro" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/76/94/veganismo-la-cultura-hegemonica-del-futuro_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/76/91/veganismo-la-cultura-hegemonica-del-futuro.jpeg" class="cs-responsive-image">
                                </a>
                            </span>
                                                <h2><a href="https://www.objetivobienestar.com/veganismo-la-cultura-hegemonica-del-futuro_42253_102.html" title="Veganismo, la cultura hegemónica del futuro">Veganismo, la cultura hegemónica del futuro</a></h2>
                                                    <h3>Muchos pensaron que era una moda pasajera, un esnobismo de nuestro tiempo que se revela contra el sistema, pero lo cierto es que hoy por hoy la opción vegetariana se implanta con fuerza en nuestra sociedad....</h3>
                                                                            <h4><a href="https://www.objetivobienestar.com/alimentacion-saludable" title="Alimentación"><span>Alimentación</span></a></h4>
                                            </div>
                </div>
                            <div class="col-xs-6 col-sm-3 col-md-2 col-lg-2">
                    <div class="item">
                                                    <span class="img">
                                <a href="https://www.objetivobienestar.com/receta-ensalada-thai_42229_102.html" title="Ensalada thai">
                                   
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/53/07/receta-ensalda-thai_3_360x213.jpeg" title="Receta Ensalda thai" alt="Receta Ensalda thai" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/53/07/receta-ensalda-thai_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/53/04/receta-ensalda-thai.jpeg" class="cs-responsive-image">
                                </a>
                            </span>
                                                <h2><a href="https://www.objetivobienestar.com/receta-ensalada-thai_42229_102.html" title="Ensalada thai">Ensalada thai</a></h2>
                                                    <h3>Una ensalada diferente, colorida y sabrosa para incluir más vegetales crudos a nuestra alimentación.</h3>
                                                                            <h4><a href="https://www.objetivobienestar.com/alimentacion-saludable" title="Alimentación"><span>Alimentación</span></a></h4>
                                            </div>
                </div>
                            <div class="col-xs-6 col-sm-3 col-md-2 col-lg-2">
                    <div class="item">
                                                    <span class="img">
                                <a href="https://www.objetivobienestar.com/receta-delicioso-brownie-vegano-solo-tres-ingredientes_42228_102.html" title="El delicioso brownie vegano de solo tres ingredientes">
                                   
        
    <img  src="https://www.objetivobienestar.com/uploads/s1/91/52/81/el-delicioso-brownie-vegano-de-solo-tres-ingredientes_3_360x213.jpeg" title="El delicioso brownie vegano de solo tres ingredientes" alt="El delicioso brownie vegano de solo tres ingredientes" height="" width="" data-prosrcset="360|213://www.objetivobienestar.com/uploads/s1/91/52/81/el-delicioso-brownie-vegano-de-solo-tres-ingredientes_3_360x213.jpeg" data-original="https://www.objetivobienestar.com/uploads/s1/91/52/78/el-delicioso-brownie-vegano-de-solo-tres-ingredientes.jpeg" class="cs-responsive-image">
                                </a>
                            </span>
                                                <h2><a href="https://www.objetivobienestar.com/receta-delicioso-brownie-vegano-solo-tres-ingredientes_42228_102.html" title="El delicioso brownie vegano de solo tres ingredientes">El delicioso brownie vegano de solo tres ingredientes</a></h2>
                                                    <h3>Sin azúcares añadidos, sin huevos, sin harina y sin mantequilla. ¿Es posible? ¡Sí! Y está increíblemente bueno. ¡Bienvenido al mundo de la repostería vegana y saludable!</h3>
                                                                            <h4><a href="https://www.objetivobienestar.com/alimentacion-saludable" title="Alimentación"><span>Alimentación</span></a></h4>
                                            </div>
                </div>
                    </div>
    </div>
    <div id="taboola-below-article-thumbnails"></div>
    <script type="text/javascript">
        window._taboola = window._taboola || [];
        _taboola.push({
            mode: 'thumbnails-a',
            container: 'taboola-below-article-thumbnails',
            placement: 'Below Article Thumbnails',
            target_type: 'mix'
        });
    </script>
</div></div>
<div class="col-xs-6 col-sm-6 col-md-2 col-lg-2 article-right"><div class="csl-inner csl-hot"><div class="col-xs-6 col-sm-3 col-md-2 col-lg-2 grid-banner">

    <div class="banner f1 v1" data-zonename="mpu1">
    
        <div id="div-gpt-ad-mpu1">
        <script>
            if (typeof googletag !== "undefined") {
                googletag.cmd.push(function () {
                    googletag.display('div-gpt-ad-mpu1');
                });
            }
        </script>
    </div>
    
</div>

    </div>
    <div class="col-xs-6 col-sm-3 col-md-2 col-lg-2" data-role="newsletter-subscription-wrapper" data-container="578381361acf5">
        <div class="subscribe" data-loading-subscribe="578381361acf5">
            <p class="title">¿Quieres aprender a vivir mejor?</p>
            <p class="subtitle">Apúntate a nuestra newsletter y recibirás los mejores consejos para ser más feliz</p>

                <form name="newsletter_form" method="post" action="javascript:void(0)" data-action="/_call?controller=ComitiumSuite%5CBundle%5CCSBundle%5CWidgets%5CNewsletterSubscription%5CController%5CWidgetController&amp;action=subscriptionAction&amp;_uuid=578381361acf5&amp;_locale=es">
            <input type="text" id="newsletter_form_name" name="newsletter_form[name]" required="required" placeholder="Nombre y apellidos" />
        

            <input type="text" id="newsletter_form_email" name="newsletter_form[email]" required="required" placeholder="Correo electrónico" />
        

        <span class="info">
            <div class="rgpd-header">
    <div>Prisma Publicaciones 2002 S.L.U., tratará los datos personales que nos facilita para informarle de noticias y contenidos, así como de ofertas en nuestros productos/servicios. Conservaremos sus datos mientras no se dé de baja o nos solicite su supresión. </div><br><div>Ud. podrá ejercer los derechos de acceso, supresión, rectificación, oposición, limitación y portabilidad mediante carta a Prisma Publicaciones 2002 S.L.U., Apartado de Correos 221 de Barcelona, o remitiendo un email a <a href="mailto:lpd@prismapublicaciones.com" target="_blank">lpd@prismapublicaciones.com</a>. Asimismo, cuando lo considere oportuno, podrá presentar una reclamación ante la Agencia Española de Protección de Datos.</div><br><div>Podrá ponerse en contacto con nuestro Delegado de Protección de Datos mediante escrito dirigido a <a href="mailto:dpo@planeta.es" target="_blank">dpo@planeta.es</a> o a Grupo Planeta, At.: Delegado de Protección de Datos, Avda. Diagonal 662-664, 08034 Barcelona.</div><br><br>
</div>


                                            
<div data-extra-form-key="finalKey" data-extra-form-value="20200526022019427995_4206975003"></div>
<div data-extra-form-key="idClausula" data-extra-form-value="67"></div>
<div data-extra-form-key="idClausulaPie" data-extra-form-value="103"></div>
<div data-extra-form-key="FGrabacion" data-extra-form-value="20200526 022019"></div>
            <br>
        </span>
                <input id="newsletter_form_submit" name="newsletter_form[submit]" type="submit" name="newsletter_form[submit]" id="newsletter_form_submit" value="Empieza ahora" />


    </form>

            <script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function() {
        var container = $('[data-container="578381361acf5"]');
        var popup = $(".lopd-popup", container);

        $(container)
            .on('submit', '[name="newsletter_form"]', function (event) {
                event.preventDefault();
                var hasRecaptcha = $('.g-recaptcha').length;
                if(hasRecaptcha) {
                    if (grecaptcha.getResponse().length===0){
                        $('.subscribe__recaptcha_error').slideDown();
                        return true;
                    }
                }

                var form = $(this),
                    widgetElem = $(this).closest('[data-role="newsletter-subscription-wrapper"]'),
                    url = form.data('action'),
                    submit = $('[type="submit"]', form).prop('disabled', true);

                widgetElem.find('[data-loading-subscribe="578381361acf5"]').addClass('loading');

                var email = widgetElem.find('#newsletter_form_email').val();


                 $('[data-extra-form-key]').each(function () {
                     if ($(this).is('input[type="checkbox"')) {
                         url = url + '&' + $(this).data('extra-form-key') + '=' + ($(this).is(':checked') ? '1' : '0');
                     } else {
                         url = url + '&' + $(this).data('extra-form-key') + '=' + $(this).data('extra-form-value');
                     }
                 });

                if (typeof email !== 'undefined' && email !== null && email !== '') {
                    $.post(url, form.serialize(), function (data) {
                        var newElement = $(data);
                        widgetElem.replaceWith(newElement).find('[data-loading-subscribe="578381361acf5"]').removeClass('loading');

                        if ($(newElement).is('form') && hasRecaptcha) {
                            if (typeof grecaptcha !== 'undefined') {
                                var captchaElement = $('.g-recaptcha', newElement),
                                    siteKey = captchaElement.data('sitekey');

                                grecaptcha.render(captchaElement.get(0), {sitekey: siteKey});
                            }
                        }
                    }).always(function () {
                        submit.prop('disabled', false);
                    })
                } else {
                    $.post(url, form.serialize(), function (data) {
                        var newElement = $(data);
                        widgetElem.replaceWith(newElement).find('[data-loading-subscribe="578381361acf5"]').removeClass('loading');
                        var hasRecaptcha = $('.g-recaptcha').length;

                        if ($(newElement).is('form') && hasRecaptcha) {
                            if (typeof grecaptcha !== 'undefined') {
                                var captchaElement = $('.g-recaptcha', newElement),
                                    siteKey = captchaElement.data('sitekey');

                                grecaptcha.render(captchaElement.get(0), {sitekey: siteKey});
                            }
                        }
                    }).always(function () {
                        submit.prop('disabled', false);
                    })
                }
            })

        //     .on('click', '.conditions', function (e) {
        //         e.preventDefault();
        //         e.stopPropagation();
        //         mostrarPopup();
        //     })
        //
        //     .on('click', '.lopd-popup .lopd-close', function (e) {
        //         cerrarPopup();
        //     });
        //
        // var mostrarPopup = function () {
        //     popup.fadeIn('slow');
        //     $('body').addClass('newmodal');
        // };
        //
        // var cerrarPopup = function () {
        //     popup.fadeOut('slow');
        //     $('body').removeClass('newmodal');
        // };
    });
</script>
        </div>
    </div>
<div class="col-xs-6 col-sm-3 col-md-2 col-lg-2">

    <div class="banner f1 v2" data-zonename="mpu2">
    
        <div id="div-gpt-ad-mpu2">
        <script>
            if (typeof googletag !== "undefined") {
                googletag.cmd.push(function () {
                    googletag.display('div-gpt-ad-mpu2');
                });
            }
        </script>
    </div>
    
</div>

    </div>
    <div class="col-xs-6 col-sm-3 col-md-2 col-lg-2">
            </div>

    <div class="col-xs-6 col-sm-3 col-md-2 col-lg-2">
        <div class="article-related">
            <h4>Te puede interesar...</h4>
                            <ul>
                                            <li><a href="https://www.objetivobienestar.com/beneficios-escritura-terapeutica-emociones_42152_102.html" title="Échales una mano a tus emociones con la escritura terapéutica">Échales una mano a tus emociones con la escritura terapéutica</a></li>
                                            <li><a href="https://www.objetivobienestar.com/entrevista-alba-usart-beuate-mediterranea_42157_102.html" title="Alba Usart: “Debemos escuchar más a nuestra piel y mirar menos nuestra edad”">Alba Usart: “Debemos escuchar más a nuestra piel y mirar menos nuestra edad”</a></li>
                                            <li><a href="https://www.objetivobienestar.com/babyccinos-cafe-descafeinado-ninos_42156_102.html" title="Babyccinos: cuando el café es cosa de niños">Babyccinos: cuando el café es cosa de niños</a></li>
                                            <li><a href="https://www.objetivobienestar.com/el-poder-terapeutico-del-cuidado-de-jardines-y-huertos-en-casa_42150_102.html" title="El poder terapéutico del cuidado de jardines y huertos en casa">El poder terapéutico del cuidado de jardines y huertos en casa</a></li>
                                            <li><a href="https://www.objetivobienestar.com/receta-quiche-esparragos-con-base-espelta-semillas_42147_102.html" title="Quiche de espárragos con base de espelta y semillas">Quiche de espárragos con base de espelta y semillas</a></li>
                                    </ul>
                    </div>
    </div>
</div></div></div></div></div>
        </div>
        <div class="row row-content">
            <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6"><div class="csl-inner csl-hot">
    <div class="banner f4 v3" data-zonename="ldb3">
    
        <div id="div-gpt-ad-ldb3">
        <script>
            if (typeof googletag !== "undefined") {
                googletag.cmd.push(function () {
                    googletag.display('div-gpt-ad-ldb3');
                });
            }
        </script>
    </div>
    
</div>    <div id="taboola-below-article-thumbnails-2nd"></div>
    <script type="text/javascript">
        window._taboola = window._taboola || [];
        _taboola.push({
            mode: 'organic-thumbnails-a',
            container: 'taboola-below-article-thumbnails-2nd',
            placement: 'Below Article Thumbnails 2nd',
            target_type: 'mix'
        });
    </script>

    <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6 article-bottom">
        <div class="tsubgroup"><span>Comentarios</span></div>
        <div class="comments">
            <div id="fb-root"></div>
            <script>
                (function(d, s, id) {
                    var js, fjs = d.getElementsByTagName(s)[0];
                    if (d.getElementById(id)) return;
                    js = d.createElement(s); js.id = id;
                    js.src = "//connect.facebook.net/es_ES/sdk.js#xfbml=1&version=v2.6";
                    fjs.parentNode.insertBefore(js, fjs);
                }(document, 'script', 'facebook-jssdk'));
            </script>
            <div class="fb-comments" data-href="https://www.objetivobienestar.com/10-comidas-sanas-que-se-preparan-en-15-minutos_10541_102.html" data-numposts="5" width="100%"></div>
        </div>
    </div>
<div class="banner f4 v2" data-zonename="ldb2">
    
        <div id="div-gpt-ad-ldb2">
        <script>
            if (typeof googletag !== "undefined") {
                googletag.cmd.push(function () {
                    googletag.display('div-gpt-ad-ldb2');
                });
            }
        </script>
    </div>
    
</div></div></div>
        </div>
    </div>
    <div class="row row-bottom">
        <div class="col-xs-6 col-sm-6 col-md-6 col-lg-6"><div class="csl-inner csl-hot">
    <footer>
        <div class="block-1">
            <div class="wrapper">

                <div class="logo">
                    <a href="/" title="Objetivo Bienestar"></a>
                </div>

                
                <div class="social">
                    <ul>
                        <li><a href="https://www.facebook.com/objetivobienestar" target="_blank" rel="nofollow" title="Facebook" class="fb"></a></li>
                        <li><a href="https://twitter.com/obienestar" target="_blank" rel="nofollow" title="Twitter" class="tw"></a></li>
                        <li><a href="https://www.instagram.com/objetivo_bienestar/" target="_blank" rel="nofollow" title="Instagram" class="ig"></a></li>
                        <li><a href="https://www.youtube.com/channel/UCab0Mt8xIaz9qQq-ilF8EAQ" target="_blank" rel="nofollow" title="You Tube" class="yt"></a></li>
                    </ul>
                                    </div>

            </div>
        </div>
        <div class="block-2">
            <div class="wrapper">
                <ul>
                    <li class="prisma">
                        <a href="http://www.prismapublicaciones.com" title="Prisma Publicaciones" target="_blank">
                            <img src="/bundles/cs/Widgets/Footer/images/logo-prisma.svg" alt="Footer.link.prisma.title" title="Footer.link.prisma.title">
                        </a>
                    </li>
                    <li>
                        <a href="https://www.objetivobienestar.com" title="Objetivo Bienestar" target="_blank">
                            <img src="/bundles/cs/Widgets/Footer/images/logo-obienestar.png" alt="Footer.link.objetivo.title" title="Footer.link.objetivo.title">
                        </a>
                    </li>
                    <li>
                        <a href="http://www.revistainteriores.es" title="Revista Interiores" target="_blank">
                            <img src="/bundles/cs/Widgets/Footer/images/logo-interiores.svg" alt="Footer.link.interiores.title" title="Footer.link.interiores.title">
                        </a>
                    </li>
                                        <li>
                        <a href="http://www.revistaañocero.com" title="Año/cero" target="_blank">
                            <img src="/bundles/cs/Widgets/Footer/images/logo-acero.svg" alt="Footer.link.cero.title" title="Footer.link.cero.title">
                        </a>
                    </li>
                    <li>
                        <a href="http://www.revistaenigmas.com" title="Enigmas" target="_blank">
                            <img src="/bundles/cs/Widgets/Footer/images/logo-enigmas.png" alt="Footer.link.enigmas.title" title="Footer.link.enigmas.title">
                        </a>
                    </li>
                     <li>
                        <a href="http://www.historiadeiberiavieja.com" title="Historia de Iberia Vieja" target="_blank">
                            <img src="/bundles/cs/Widgets/Footer/images/logo-hiv.svg" alt="Footer.link.iberia.title" title="Footer.link.iberia.title">
                        </a>
                    </li>
                                    </ul>
            </div>
        </div>
        <div class="block-3">
            <div class="wrapper">
                <ul>
                    <li>© Editorial Planeta, S.A.U. 2020</li>
                    <li><a href="/sobre-nosotros.html" title="Sobre nosotros">Sobre nosotros</a></li>
                    <li><a href="/contacto.html" title="Contacto">Contacto</a></li>
                    <li><a href="/publicidad.html" title="Publicidad">Publicidad</a></li>
                    <li><a href="/condiciones-de-uso.html" title="Condiciones de uso">Condiciones de uso</a></li>
                    <li><a href="/politica-de-cookies.html" title="Política de cookies">Política de cookies</a></li>
                    <li><a href="/politica-de-privacidad.html" title="Política de privacidad">Política de privacidad</a></li>
                </ul>
            </div>
        </div>
    </footer>

</div></div>
    </div>
    <script type='text/javascript'>
    document.addEventListener("DOMContentLoaded", function(event) {
        var p='96061',s='objetivobienestar',e='smartIntxt',c='';
        var t='//des.smartclip.net/ads?type=dyn&sz=400x320&plc='+p+'&sc_sitName='+s+'&elementId='+e+'&cat='+c;
        t+='&ref='+encodeURIComponent(window.top.document.URL);t+='&rnd='+Math.round(Math.random()*1e8);
        var n=document.createElement('script');n.type='text/javascript';n.src=t;document.body.appendChild(n);
    });
    </script>
        </div>
        <a href="javascript:void(0);" title="Subir" class="scrollup"></a>
    </div>

        <!-- <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-572b79c9597919be"></script> -->
        <script type="text/javascript">_satellite.pageBottom();</script>
    
    <!-- Taboola -->
    <script type="text/javascript">
        window._taboola = window._taboola || [];
        _taboola.push({flush: true});
    </script>
		
	<script type="text/javascript" src="/js/fe6d422.js?v=5ebe8dec76e87"></script>

<script type="text/javascript" src="/js/00a7357.js?v=5ebe8dec913dc"></script>	</body>
</html>

"""))

if __name__ == "__main__":
    main()

