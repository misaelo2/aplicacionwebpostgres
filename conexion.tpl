<!DOCTYPE HTML>
<html>

<table class="egt">

  		<tr>

   			 <th>Codigo</th>
    			 <th>Nombre</th>
			 <th>Tipo</th>

  		</tr>


%for elem in datos :
		<tr>
    	 	 <td>{{elem["codigo"]}}</td>
   		 <td>{{elem["nombre"]}}</td>
    		 <td>{{elem["tipo"]}}</td>
		</tr>
%end
</end table>
