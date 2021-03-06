# encoding: utf-8
"""
Create on: 2018-09-24 下午3:41
author: sato
mail: ysudqfs@163.com
life is short, you need python
"""
services = {
    "base":  [
        {
            "name":     "mysql",
            "port":     "3306",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/data/mysql/",
            "logindex": "error.log",
            "logs":     [],
            "comment":  "数据库DB服务"
        },
        {
            "name":     "redis-server",
            "port":     "6379",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/data/redis/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "缓存服务"
        },
        {
            "name":     "mongodb",
            "port":     "27017",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/data/redis/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "Mongodb"
        },
        {
            "name":     "apache2",
            "port":     "90",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/data/redis/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "阿帕奇"
        },
        {
            "name":     "zookeeper",
            "port":     "11100",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/data/zklog/version-2/",
            "logindex": "*",
            "logs":     [],
            "comment":  "KAFKAMQ管理服务"
        },
        {
            "name":     "kafka",
            "port":     "11090",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/im/vrv/kafka/logs/",
            "logindex": "controller.log kafka-authorizer.log kafka-request.log kafkaServer-gc.log log-cleaner.log "
                        "server.log state-change.log zookeeper-gc.log",
            "logs":     [],
            "comment":  "消息队列MQ服务"
        },
        {
            "name":     "elasticsearch",
            "port":     "11110",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/im/vrv/elasticsearch/logs/",
            "logindex": "linkdood_index_data_deprecation linkdood_index_data_index_indexing_slowlog "
                        "linkdood_index_data_index_search_slowlog linkdood_index_data.log",
            "logs":     [],
            "comment":  "全文检索服务"
        },
        {
            "name":     "turnserver",
            "port":     "10660",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/turnserver/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "打洞服务"
        },
        {
            "name":     "fdfs_trackerd",
            "port":     "11060",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/data/fdfs_trackerd/logs/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "存储调度服务"
        },
        {
            "name":     "fdfs_storaged",
            "port":     "11070",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/data/fdfs_storaged/logs/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "储存服务"
        },
        {
            "name":     "tomcat-webapp",
            "port":     "11307",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/tomcat-webapp/",
            "logindex": "catalina.*",
            "logs":     [],
            "comment":  "后台管理服务"
        },
        {
            "name":     "tomcat-app",
            "port":     "11310",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/tomcat-app/",
            "logindex": "catalina.*",
            "logs":     [],
            "comment":  "应用服务"
        },
        {
            "name":     "nginx",
            "port":     "80",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/nginx/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "WEB服务"
        },
    ],
    "cpp":   [
        {
            "name":     "prelogin",
            "port":     "11010",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/prelogin/",
            "logindex": "info.log*",
            "logs":     [],
            "comment":  "预登录服务"
        },
        #    {
        #        "name":"prelogin_old",
        #        "port":"5000",
        #        "status":"",
        #        "pid":"",
        #        "logdir":"/data/linkdood/logs/prelogin_old/",
        #        "logindex":"info.log*",
        #        "logs":[],
        #        "comment":"旧版本预登录服务"
        #    },
        {
            "name":     "upload",
            "port":     "11040",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/upload/",
            "logindex": "upload.log*",
            "logs":     [],
            "comment":  "文件服务"
        },
        {
            "name":     "ap",
            "port":     "11130",  # inside_port:11150	outside_port:11130	web_port:11140
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/ap/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "AP服务"
        },
        {
            "name":     "badword",
            "port":     "11040",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/badword/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "关键词服务"
        },
        {
            "name":     "go-mail",
            "port":     "11050",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/mail/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "邮件服务"
        },
        {
            "name":     "apnsAgentConfig",
            "port":     "11020",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/apnsAgentConfig/",
            "logindex": "*.log",
            "logs":     [],
            "comment":  "推送代理服务"
        },
    ],
    "java":  [
        {
            "name":     "server-config",
            "port":     "8999",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-config*",
            "logs":     [],
            "comment":  "基础配置服务"
        },
        {
            "name":     "server-dbconfig",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-dbconfigServer*",
            "logs":     [],
            "comment":  "数据库配置服务"
        },
        {
            "name":     "server-timestamp",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-timeStampServer*",
            "logs":     [],
            "comment":  "时间戳服务"
        },
        {
            "name":     "server-fullsearch",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-fullSearchServer*",
            "logs":     [],
            "comment":  "全文检索服务"
        },
        {
            "name":     "server-userbase",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-platform-database*",
            "logs":     [],
            "comment":  "用户基础服务"
        },
        {
            "name":     "server-platform-database",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-commentCenterServer*",
            "logs":     [],
            "comment":  "企业数据字典服务"
        },
        {
            "name":     "server-login",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-loginServer*",
            "logs":     [],
            "comment":  "登录服务"
        },
        {
            "name":     "server-online",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-onlineServer*",
            "logs":     [],
            "comment":  "用户在线服务"
        },
        {
            "name":     "server-chat",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-chatServer*",
            "logs":     [],
            "comment":  "聊天服务"
        },
        {
            "name":     "server-route",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-routeServer*",
            "logs":     [],
            "comment":  "消息路由服务"
        },
        {
            "name":     "server-messagestorage",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-messageStorageServer*",
            "logs":     [],
            "comment":  "消息存贮服务"
        },
        {
            "name":     "server-imageverify",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-imageVerifyServer*",
            "logs":     [],
            "comment":  "图片验证码服务"
        },
        {
            "name":     "server-buddy",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-buddyServer*",
            "logs":     [],
            "comment":  "好友服务"
        },
        {
            "name":    "server-buddyverify",
            "port":    "",
            "status":  "",
            "pid":     "",
            "logdir":  "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logidex": "*",
            "logs":    [],
            "comment": "好友验证服务"
        },
        {
            "name":     "server-verifybox",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-verifyboxServer*",
            "logs":     [],
            "comment":  "验证盒子服务"
        },
        {
            "name":     "server-registeruser",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-registerUserServer*",
            "logs":     [],
            "comment":  "用户注册服务"
        },
        {
            "name":     "server-recommend",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-recommendServer*",
            "logs":     [],
            "comment":  "好友推荐服务"
        },
        {
            "name":     "server-setting",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-settingServer*",
            "logs":     [],
            "comment":  "用户设置服务"
        },
        {
            "name":     "server-group",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-groupServer*",
            "logs":     [],
            "comment":  "群服务"
        },
        {
            "name":     "server-groupfile",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-groupFileServer*",
            "logs":     [],
            "comment":  "群文件服务"
        },
        {
            "name":     "server-groupmember",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-groupMemberServer*",
            "logs":     [],
            "comment":  "群成员服务"
        },
        {
            "name":     "server-groupverify",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-groupVerifyServer*",
            "logs":     [],
            "comment":  "群验证服务"
        },
        {
            "name":     "server-enterpriseregister",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-enterpriseregister*",
            "logs":     [],
            "comment":  "企业用户注册服务"
        },
        {
            "name":     "server-enterpriseuser",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-enterpriseuser*",
            "logs":     [],
            "comment":  "企业用户服务"
        },
        {
            "name":     "server-enterpriserolemenu",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-enterpriserolemenu*",
            "logs":     [],
            "comment":  "角色菜单服务"
        },
        {
            "name":     "server-analysiswebsite",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-analysiswebsite*",
            "logs":     [],
            "comment":  "网址解析服务"
        },
        {
            "name":     "server-memo",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-memo*",
            "logs":     [],
            "comment":  "备忘录服务"
        },
        {
            "name":     "server-verifycode",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-verifyCodeServer*",
            "logs":     [],
            "comment":  "验证码服务"
        },
        {
            "name":     "server-iosnotice",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-iosNoticeServer*",
            "logs":     [],
            "comment":  "消息推送服务"
        },
        {
            "name":     "server-task",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-task*",
            "logs":     [],
            "comment":  "任务投票"
        },
        {
            "name":     "server-emoticon",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-emoticonServer*",
            "logs":     [],
            "comment":  "表情包服务"
        },
        {
            "name":     "server-operationlog",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-operation*",
            "logs":     [],
            "comment":  "日志服务"
        },
        {
            "name":     "server-platform",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-platformServer*",
            "logs":     [],
            "comment":  "开发平台服务"
        },
        {
            "name":     "server-enterprisetask",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-enterprisetask*",
            "logs":     [],
            "comment":  "任务管理"
        },
        {
            "name":     "server-lbs",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-lbsServer*",
            "logs":     [],
            "comment":  "位置服务"
        },
        {
            "name":     "server-collection",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-collection*",
            "logs":     [],
            "comment":  "数据收集"
        },
        {
            "name":     "server-feedback",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-feedback*",
            "logs":     [],
            "comment":  "反馈服务"
        },
        {
            "name":     "server-commentcenter",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-commentCenterServer*",
            "logs":     [],
            "comment":  "评论中心服务"
        },
        {
            "name":     "server-share",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-shareContentServer*",
            "logs":     [],
            "comment":  "分享服务"
        },
        {
            "name":     "server-enterprisestatistics",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/data/linkdood/logs/javaserver/",
            "logindex": "server-enterprisestatistics*",
            "logs":     [],
            "comment":  "后台统计服务"
        },
        {
            "name":     "server-enterprisechat",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-enterprisechat*",
            "logs":     [],
            "comment":  "视频分控服务"
        },
        {
            "name":     "server-unreadmsgpush",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-unreadmsgpush*",
            "logs":     [],
            "comment":  "短信发送服务"
        },
        {
            "name":     "server-platformstatistics",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-platformstatistics*",
            "logs":     [],
            "comment":  "阅读统计服务"
        },
        {
            "name":     "server-vrvxin",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-vrvxin*",
            "logs":     [],
            "comment":  "公共服务平台基础服务"
        },
        {
            "name":     "server-sharecomment",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-shareCommentServer*",
            "logs":     [],
            "comment":  "朋友圈服务"
        },
        {
            "name":     "server-cloud",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-cloud*",
            "logs":     [],
            "comment":  "云盘管理服务"
        },
        {
            "name":     "server-imuser",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-userServer*",
            "logs":     [],
            "comment":  "用户二级服务"
        },
        {
            "name":     "server-platform-business",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-platform-business*",
            "logs":     [],
            "comment":  "公众平台服务"
        },
        {
            "name":     "server-enterpriseorganization",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-enterpriseorganizationServer*",
            "logs":     [],
            "comment":  "组织机构服务"
        },
        {
            "name":     "server-verifymessage",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-verifyMessageServer*",
            "logs":     [],
            "comment":  "消息盒子服务"
        },
        {
            "name":     "server-cache",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "/home/kali/Desktop/keke/data/linkdood/logs/javaserver/",
            "logindex": "server-cacheServer*",
            "logs":     [],
            "comment":  "缓存服务"
        },
    ],
    "merge": [
        {
            "name":     "cj",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "",
            "logindex": "",
            "logs":     [],
            "comment":  "C++及java服务"
        },
        {
            "name":     "java",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "",
            "logindex": "",
            "logs":     [],
            "comment":  "java服务"
        },
        {
            "name":     "all",
            "port":     "",
            "status":   "",
            "pid":      "",
            "logdir":   "",
            "logindex": "",
            "logs":     [],
            "comment":  "全部服务"
        },
    ]
}
