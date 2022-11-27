// JavaScript source code
Dropzone.autoDiscover = false;
const myDropzone = new Dropzone('#my-dropzone', {
    url: 'upload/',
    maxFiles: 12,
    acceptedFiles: `image/*,.jpg,.jpeg,.png`,
    clickable: true,
})