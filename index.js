// This file is used to register all your cloud functions in GCP.
// DO NOT EDIT/DELETE THIS, UNLESS YOU KNOW WHAT YOU ARE DOING.

exports.superresolutionfunction = require("./superresolution/function.js").handler;
exports.superresolutionsuperresolutionuploadimage = require("./superresolution/superresolution_upload_image.py").handler;