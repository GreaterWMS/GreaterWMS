function a(n,e,t){return t<=e?e:Math.min(t,Math.max(e,n))}function u(n,e,t){if(t<=e)return e;const o=t-e+1;let r=e+(n-e)%o;return r<e&&(r=o+r),r===0?0:r}export{a as b,u as n};
