"use strict";

var canvas;
var gl;
var program;
var texture;

var NumVertices  = 18;
var texSize = 32;

var pointsArray = [];
var colorsArray = [];
var texCoordsArray = [];

var xAxis = 0;
var yAxis = 1;
var zAxis = 2;
var axis = 0;
var theta = [ 45, 45, 45 ];

var thetaLoc;

var texCoord = [
    vec2(    0,   0 ), vec2( 0.33,   0 ), vec2( 0.17, 0.5 ),
    vec2( 0.33,   0 ), vec2( 0.66,   0 ), vec2(  0.5, 0.5 ),
    vec2(    0, 0.5 ), vec2( 0.33, 0.5 ), vec2( 0.17,   1 ),
    vec2( 0.33, 0.5 ), vec2( 0.66, 0.5 ), vec2(  0.5,   1 ),
    vec2( 0.66, 0.5 ), vec2( 0.66,   0 ), vec2(    1,   0 ), vec2(    1, 0.5 )
];

// 좌표 설정
var vertices = [
    vec4(    0,  0.5,    0, 1.0 ),
    vec4( -0.5, -0.5, -0.5, 1.0 ),
    vec4(  0.5, -0.5, -0.5, 1.0 ),
    vec4(  0.5, -0.5,  0.5, 1.0 ),
    vec4( -0.5, -0.5,  0.5, 1.0 )
];

var vertexColors = [
    vec4( 1.0, 0.0, 0.0, 1.0 ),  // red
    vec4( 1.0, 1.0, 0.0, 1.0 ),  // yellow
    vec4( 0.0, 1.0, 0.0, 1.0 ),  // green
    vec4( 0.0, 0.0, 1.0, 1.0 ),  // blue
    vec4( 1.0, 0.0, 1.0, 1.0 ),  // magenta
    vec4( 0.0, 1.0, 1.0, 1.0 ),  // white
    vec4( 0.0, 1.0, 1.0, 1.0 )   // cyan
];


function configureTexture( image ) {
    texture = gl.createTexture();
    gl.bindTexture( gl.TEXTURE_2D, texture );
    gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
    gl.texImage2D( gl.TEXTURE_2D, 0, gl.RGB,
         gl.RGB, gl.UNSIGNED_BYTE, image );
    gl.generateMipmap( gl.TEXTURE_2D );
    gl.texParameteri( gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER,
                      gl.NEAREST_MIPMAP_LINEAR );
    gl.texParameteri( gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST );

    gl.uniform1i(gl.getUniformLocation(program, "texture"), 0);
}

// 총 6개의 삼각형으로 피라미드를 만든다.
// (2, 1, 4), (2, 4, 3) 두 개의 삼각형이 합쳐져 사각형인 밑면이 만들어진다.
function colorCube()
{
    pyramid(2, 1, 0)
    pyramid(3, 2, 0)
    pyramid(4, 3, 0)
    pyramid(1, 4, 0)
    pyramid(2, 1, 4, 3)
}

function pyramid(a, b, c, d)
{
    var arr = [a, b, c];

    if (c == 4) {
        pointsArray.push(vertices[a]);
        colorsArray.push(vertexColors[0]);
        texCoordsArray.push(texCoord[12]);

        pointsArray.push(vertices[b]);
        colorsArray.push(vertexColors[0]);
        texCoordsArray.push(texCoord[13]);

        pointsArray.push(vertices[c]);
        colorsArray.push(vertexColors[0]);
        texCoordsArray.push(texCoord[14]);

        pointsArray.push(vertices[a]);
        colorsArray.push(vertexColors[0]);
        texCoordsArray.push(texCoord[12]);

        pointsArray.push(vertices[c]);
        colorsArray.push(vertexColors[0]);
        texCoordsArray.push(texCoord[14]);

        pointsArray.push(vertices[d]);
        colorsArray.push(vertexColors[0]);
        texCoordsArray.push(texCoord[15]);
    }
    else {
        if (b == 1) {
            for (var i = 0; i < 3; i++) {
                pointsArray.push(vertices[arr[i]]);
                colorsArray.push(vertexColors[a]);
                texCoordsArray.push(texCoord[i]);
            }
        }
        else if (b == 2) {
            for (var i = 0; i < 3; i++) {
                pointsArray.push(vertices[arr[i]]);
                colorsArray.push(vertexColors[a]);
                texCoordsArray.push(texCoord[i+3]);
            }
        }
        else if (b == 3) {
            for (var i = 0; i < 3; i++) {
                pointsArray.push(vertices[arr[i]]);
                colorsArray.push(vertexColors[a]);
                texCoordsArray.push(texCoord[i+6]);
            }
        }
        else {
            for (var i = 0; i < 3; i++) {
                pointsArray.push(vertices[arr[i]]);
                colorsArray.push(vertexColors[a]);
                texCoordsArray.push(texCoord[i+9]);
            }
        }
    }
}

window.onload = function init()
{
    canvas = document.getElementById( "gl-canvas" );

    gl = WebGLUtils.setupWebGL( canvas );
    if ( !gl ) { alert( "WebGL isn't available" ); }

    gl.viewport( 0, 0, canvas.width, canvas.height );
    gl.clearColor( 1.0, 1.0, 1.0, 1.0 );

    gl.enable(gl.DEPTH_TEST);

    //
    //  Load shaders and initialize attribute buffers
    //
    program = initShaders( gl, "vertex-shader", "fragment-shader" );
    gl.useProgram( program );

    colorCube();

    var cBuffer = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, cBuffer );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(colorsArray), gl.STATIC_DRAW );

    var vColor = gl.getAttribLocation( program, "vColor" );
    gl.vertexAttribPointer( vColor, 4, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vColor );

    var vBuffer = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, vBuffer );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(pointsArray), gl.STATIC_DRAW );

    var vPosition = gl.getAttribLocation( program, "vPosition" );
    gl.vertexAttribPointer( vPosition, 4, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vPosition );

    var tBuffer = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, tBuffer );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(texCoordsArray), gl.STATIC_DRAW );

    var vTexCoord = gl.getAttribLocation( program, "vTexCoord" );
    gl.vertexAttribPointer( vTexCoord, 2, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vTexCoord );


    var image = document.getElementById("texImage");
    configureTexture(image);

    thetaLoc = gl.getUniformLocation(program, "theta");

    //event listeners for buttons

    document.getElementById( "xButton" ).onclick = function () {
        axis = xAxis;
    };
    document.getElementById( "yButton" ).onclick = function () {
        axis = yAxis;
    };
    document.getElementById( "zButton" ).onclick = function () {
        axis = zAxis;
    };

    render();
}

var render = function()
{
    gl.clear( gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    theta[axis] += 2.0;
    gl.uniform3fv(thetaLoc, theta);

    gl.drawArrays( gl.TRIANGLES, 0, NumVertices );

    requestAnimFrame( render );
}