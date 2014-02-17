% import time
% import uuid
% for item in items :
%   if content :
<div class="well">
%   else :
%       tempItemId = uuid.uuid1()
<div class="panel panel-default">
    <div class="panel-heading">
        <a class="panel-title" data-toggle="collapse" data-parent="#itemContainer"
            href="#{{tempItemId}}">
            <h5>{{!item[3]}}</h5>
        </a>
    </div>
    <div class="panel-collapse collapse" id="{{tempItemId}}" style="height: 0px; ">
        <div class="panel-body">
%   end
<p>{{time.strftime('%a, %d %b %Y %H:%M:%S', time.gmtime(float(item[1])))}}</p>
<a href={{!item[4]}} target="_blank"><p class="lead">{{!item[3]}}</p></a>
<p>from : {{!item[2]}}</p>
<div style="word-break:break-all">{{!item[5]}}</div>
%   if content :
</div>
%   else :
        </div>
    </div>
</div>
%   end
% end