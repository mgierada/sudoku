function draw() {
    var canvas = document.getElementById('myCanvas');
    if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        drawBoard(ctx) 
    //    ctx.moveTo(0, 0);
    //    ctx.lineTo(0, 400);
    //    ctx.stroke();
    //    ctx.fillStyle = "#FF0000";
    //    ctx.fillRect(0, 0, 150, 75);
    }
}
function drawBoard(ctx) {
    for (let i = 0; i <= 9; i++) {
        let col = 40 * i
        ctx.moveTo(col, 0);
        ctx.lineTo(col, 360);
        ctx.stroke();
    }
    for (let i = 0; i <= 9; i++) {
     let row = 40 * i
     ctx.moveTo(0, row);
     ctx.lineTo(360, row);
     ctx.stroke();
 }
}
draw()