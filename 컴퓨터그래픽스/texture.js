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
    vec2(   0,  0 ),
    vec2(   0,  1 ),
    vec2(   1,  1 ),
    vec2(   1,  0 ),
    vec2( 0.5,  1 )
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

function colorCube()
{
    pyramid(1, 2, 0)
    pyramid(0, 2, 3)
    pyramid(3, 4, 0)
    pyramid(4, 1, 0)
    pyramid(2, 1, 4, 3)
}

function pyramid(a, b, c, d)
{
    if (d) {
        pointsArray.push(vertices[a]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[1]);

        pointsArray.push(vertices[b]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[0]);

        pointsArray.push(vertices[c]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[3]);

        pointsArray.push(vertices[a]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[1]);

        pointsArray.push(vertices[c]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[3]);

        pointsArray.push(vertices[d]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[2]);
    }
    else {
        pointsArray.push(vertices[a]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[0]);

        pointsArray.push(vertices[b]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[3]);

        pointsArray.push(vertices[c]);
        colorsArray.push(vertexColors[a]);
        texCoordsArray.push(texCoord[4]);
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

    var image = document.getElementById("texImage1");
    configureTexture(image);

    document.getElementById("texImage1").onclick = function() {
        configureTexture(document.getElementById("texImage1"));
    };
    document.getElementById("texImage2").onclick = function() {
        configureTexture(document.getElementById("texImage2"));
    };
    document.getElementById("texImage3").onclick = function() {
        configureTexture(document.getElementById("texImage3"));
    };
    document.getElementById("texImage4").onclick = function() {
        configureTexture(document.getElementById("texImage4"));
    };
    document.getElementById("texImage5").onclick = function() {
        configureTexture(document.getElementById("texImage5"));
    };
    document.getElementById("texImage6").onclick = function() {
        configureTexture(document.getElementById("texImage6"));
    };

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