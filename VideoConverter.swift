import Foundation
import FFmpegKit

class VideoConverter {

    func extractAudio(inputPath: String, outputPath: String, completion: @escaping (Bool) -> Void) {
        let cmd = "-i \(inputPath) -vn -acodec libmp3lame -y \(outputPath)"
        FFmpegKit.executeAsync(cmd) { session in
            let returnCode = session?.getReturnCode()
            completion(returnCode?.isValueSuccess ?? false)
        }
    }

    func compressVideo(inputPath: String,
                       outputPath: String,
                       crf: Int = 28,
                       preset: String = "medium",
                       targetWidth: Int? = nil,
                       completion: @escaping (Bool) -> Void) {
        var scaleFilter = "format=yuv420p"
        if let width = targetWidth {
            scaleFilter += ",scale=\(width):-2"
        }
        let cmd = "-i \(inputPath) -vcodec libx264 -crf \(crf) -preset \(preset) -acodec aac -movflags +faststart -vf \(scaleFilter) -y \(outputPath)"
        FFmpegKit.executeAsync(cmd) { session in
            let returnCode = session?.getReturnCode()
            completion(returnCode?.isValueSuccess ?? false)
        }
    }

    func convertVideo(inputPath: String,
                      outputPath: String,
                      targetWidth: Int? = nil,
                      completion: @escaping (Bool) -> Void) {
        var scaleFilter = "format=yuv420p"
        if let width = targetWidth {
            scaleFilter += ",scale=\(width):-2"
        }
        let cmd = "-i \(inputPath) -c:v libx264 -c:a aac -movflags +faststart -vf \(scaleFilter) -y \(outputPath)"
        FFmpegKit.executeAsync(cmd) { session in
            let returnCode = session?.getReturnCode()
            completion(returnCode?.isValueSuccess ?? false)
        }
    }

    func videoToGif(inputPath: String,
                    outputPath: String,
                    startTime: String? = nil,
                    duration: Int? = nil,
                    width: Int = 320,
                    completion: @escaping (Bool) -> Void) {
        var cmd = "-i \(inputPath) "
        if let ss = startTime {
            cmd += "-ss \(ss) "
        }
        if let t = duration {
            cmd += "-t \(t) "
        }
        cmd += "-vf fps=15,scale=\(width):-1:flags=lanczos -y \(outputPath)"
        FFmpegKit.executeAsync(cmd) { session in
            let returnCode = session?.getReturnCode()
            completion(returnCode?.isValueSuccess ?? false)
        }
    }
}
