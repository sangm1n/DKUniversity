
var gl;
var points = [];

var divideCount = 4;

window.onload = function init()
{
    var canvas = document.getElementById( "gl-canvas" );
    
    gl = WebGLUtils.setupWebGL( canvas );
    if ( !gl ) { alert( "WebGL isn't available" ); }

    
    // Four Vertices
    var vertices = [
        vec2( -1, 1 ),
        vec2(  -1, -1 ),
        vec2(  1, -1 ),
        vec2( 1, 1 )
    ];

    divideSquare(vertices[0], vertices[1], vertices[2], vertices[3], divideCount);

    //
    //  Configure WebGL
    //
    gl.viewport( 0, 0, canvas.width, canvas.height );
    gl.clearColor( 0.0, 0.0, 0.0, 1.0 );
    
    //  Load shaders and initialize attribute buffers
    
    var program = initShaders( gl, "vertex-shader", "fragment-shader" );
    gl.useProgram( program );
    
    // Load the data into the GPU
    
    var bufferId = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, bufferId );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(points), gl.STATIC_DRAW );

    // Associate out shader variables with our data buffer
    
    var vPosition = gl.getAttribLocation( program, "vPosition" );
    gl.vertexAttribPointer( vPosition, 2, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vPosition );

    render();
};

function square(a, b, c, d) {
    points.push(a, b, d);
    points.push(b, c, d);
}

function divideSquare(a, b, c, d, count) {
    if (count == 0) {
        square(a, b, c, d);
    }
    else {
        var ab1 = mix(a, b, 0.33);
        var ab2 = mix(a, b, 0.67);
        var bc1 = mix(b, c, 0.33);
        var bc2 = mix(b, c, 0.67);
        var cd1 = mix(c, d, 0.33);
        var cd2 = mix(c, d, 0.67);
        var ad1 = mix(a, d, 0.33);
        var ad2 = mix(a, d, 0.67);

        var ac1 = mix(a, c, 0.33);
        var ac2 = mix(a, c, 0.67);
        var bd1 = mix(b, d, 0.33);
        var bd2 = mix(b, d, 0.67);

        --count;

        divideSquare(a, ab1, ac1, ad1, count);
        divideSquare(ab1, ab2, bd1, ac1, count);
        divideSquare(ab2, b, bc1, bd1, count);
        divideSquare(ad1, ac1, bd2, ad2, count);
        divideSquare(bd1, bc1, bc2, ac2, count);
        divideSquare(ad2, bd2, cd2, d, count);
        divideSquare(bd2, ac2, cd1, cd2, count);
        divideSquare(ac2, bc2, c, cd1, count);
    }
}


function render() {
    gl.clear( gl.COLOR_BUFFER_BIT );
    gl.drawArrays( gl.TRIANGLES, 0, points.length );
}