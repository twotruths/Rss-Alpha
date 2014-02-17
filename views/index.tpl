<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh" lang="zh">
<head>
    <title>Rss Alpha</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <script src="js/jquery.min.js"></script>

    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- <link rel="stylesheet" href="css/bootstrap-theme.min.css"> -->
    <link href="css/todc-bootstrap.min.css" rel="stylesheet">
    <!-- <link rel="stylesheet" href="css/font-awesome.min.css"> -->
    <script src="js/bootstrap.min.js"></script>

    <script type="text/javascript" src="js/rss.js"></script>
    <link rel="stylesheet" type="text/css" href="css/rss.css">
</head>
<body>
% include('nav.tpl')
% include('itemList.tpl', items = items)
</body>
</html>
