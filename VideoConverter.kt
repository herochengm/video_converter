package com.example.videotools

import android.content.Context
import com.arthenica.ffmpegkit.FFmpegKit
import com.arthenica.ffmpegkit.ReturnCode
import java.io.File

class VideoConverter(private val context: Context) {

    fun extractAudio(inputPath: String, outputPath: String, callback: (success: Boolean) -> Unit) {
        val cmd = "-i $inputPath -vn -acodec libmp3lame -y $outputPath"
        FFmpegKit.executeAsync(cmd) { session ->
            val returnCode = session.returnCode
            callback(returnCode.isValueSuccess)
        }
    }

    fun compressVideo(
        inputPath: String,
        outputPath: String,
        crf: Int = 28,
        preset: String = "medium",
        width: Int? = null,
        callback: (success: Boolean) -> Unit
    ) {
        val scale = width?.let { ",scale=$it:-2" } ?: ""
        val cmd = "-i $inputPath -vcodec libx264 -crf $crf -preset $preset -acodec aac -movflags +faststart -vf format=yuv420p$scale -y $outputPath"
        FFmpegKit.executeAsync(cmd) { session ->
            val returnCode = session.returnCode
            callback(returnCode.isValueSuccess)
        }
    }

    fun convertVideo(
        inputPath: String,
        outputPath: String,
        width: Int? = null,
        callback: (success: Boolean) -> Unit
    ) {
        val scale = width?.let { ",scale=$it:-2" } ?: ""
        val cmd = "-i $inputPath -c:v libx264 -c:a aac -movflags +faststart -vf format=yuv420p$scale -y $outputPath"
        FFmpegKit.executeAsync(cmd) { session ->
            val returnCode = session.returnCode
            callback(returnCode.isValueSuccess)
        }
    }

    fun videoToGif(
        inputPath: String,
        outputPath: String,
        startTime: String? = null,
        duration: Int? = null,
        width: Int = 320,
        callback: (success: Boolean) -> Unit
    ) {
        val ss = startTime?.let { "-ss $it" } ?: ""
        val t = duration?.let { "-t $it" } ?: ""
        val vf = "fps=15,scale=$width:-1:flags=lanczos"
        val cmd = "-i $inputPath $ss $t -vf $vf -y $outputPath"
        FFmpegKit.executeAsync(cmd) { session ->
            val returnCode = session.returnCode
            callback(returnCode.isValueSuccess)
        }
    }
}
