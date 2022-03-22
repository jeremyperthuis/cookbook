#ifdef GL_ES
precision mediump float;
#endif

uniform vec2 u_resolution; 

float circleShape(float radius, vec2 position){
    return step(radius, length(position-vec2(0.5)));

}

void main(){
    vec2 pixelCoord = gl_FragCoord.xy / u_resolution;
    float circle = circleShape(0.3, pixelCoord);
    vec3 color = vec3(circle);
    gl_FragColor = vec4(color, 1.0);
}