program Hello;
uses Crt;
var i: integer;
begin
    for i:=0 to 15 do
    begin
        textColor(i);
        writeln(i);
    end;
    for i:=0 to 15 do
    begin
        textBackground(i);
        writeln(i);
    end;
    readln;
end.
