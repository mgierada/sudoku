function draw() {
    const canvas = document.getElementById('myCanvas');
    var array = [
        [6, 3, 0, 5, 0, 0, 0, 0, 0],
        [8, 1, 0, 6, 4, 9, 5, 0, 2],
        [5, 0, 0, 0, 3, 2, 0, 1, 6],
        [0, 0, 8, 0, 2, 0, 0, 0, 0],
        [0, 0, 3, 9, 0, 6, 4, 0, 1],
        [0, 5, 0, 4, 8, 1, 0, 0, 0],
        [3, 0, 0, 2, 0, 4, 8, 5, 0],
        [0, 0, 0, 0, 9, 8, 1, 6, 4],
        [0, 0, 9, 1, 6, 0, 2, 0, 0]
    ]
    if (canvas.getContext) {
        const ctx = canvas.getContext('2d');
        drawBoard(ctx) 
        printNumbers(ctx, array)
    }
}
function drawBoard(ctx) {
    for (let i = 0; i <= 9; i++) {
        let col = 40 * i
        if (i % 3 == 0 & i != 9) {
            ctx.beginPath();
            ctx.moveTo(col, 0);
            ctx.lineTo(col, 360);
            ctx.lineWidth = 4;
            ctx.stroke();
        } else {
            ctx.beginPath();
            ctx.moveTo(col, 0);
            ctx.lineTo(col, 360);
            ctx.lineWidth = 1;
            ctx.stroke();
        }        
    }
    for (let i = 0; i <= 9; i++) {
        let row = 40 * i
        if (i % 3 == 0 & i!=9) {
                ctx.beginPath()
                ctx.moveTo(0, row);
                ctx.lineTo(360, row);
                ctx.lineWidth = 4;
                ctx.stroke();
        } else {
                ctx.beginPath()
                ctx.moveTo(0, row);
                ctx.lineTo(360, row);
                ctx.lineWidth = 1;
                ctx.stroke();
        }
    }
}

function printNumbers(ctx, array) {
    for (let index1 = 0; index1 < 9; index1++) {
        for (let index2 = 0; index2 < 9; index2++) {
            const element = array[index1][index2];
            ctx.font = '32px Helvetica'
            if (element == 0) {
                ctx.fillText('', 12 + index2 * 40, 32 + index1*40);    
            } else {
                ctx.fillText(element, 12 + index2 * 40, 32 + index1 * 40);
            }
        }
    }
}

draw()